"""Sphinx role ``entity`` – inline ontology metadata popups.

Usage in reStructuredText or MyST Markdown::

    :entity:`SpontaneousMagnetization`

Architecture
------------
* **Python role** (this module) – resolves the ontology label via
  ``mammos_entity.Entity``, builds a popup HTML fragment, and emits two
  docutils nodes: an ``inline`` node styled as the visible text and a
  ``raw`` node containing a ``<script type="application/json">`` element
  with the popup payload.
* **JavaScript** (``_static/js/entity_tippy_click.js``) – on page load,
  finds each ``.entity-ref`` element, reads its adjacent JSON payload,
  and attaches a *tippy.js* popup.
* **CSS** (``_static/css/custom.css``) – styles the inline term
  (italic + dotted underline) and the popup card.
"""

from __future__ import annotations

import html
import json
from collections import defaultdict
from typing import TYPE_CHECKING

from docutils import nodes
from mammos_entity import Entity

if TYPE_CHECKING:
    from docutils.parsers.rst.states import Inliner
    from sphinx.application import Sphinx


def _first_value_text(value: object) -> str | None:
    """Return first non-empty string representation from scalars or sequences."""
    if isinstance(value, str):
        text = value.strip()
        return text if text else None

    try:
        iterator = iter(value)  # type: ignore[arg-type]
    except TypeError:
        text = str(value).strip()
        return text if text else None

    for item in iterator:
        text = str(item).strip()
        if text:
            return text
    return None


def _display_name(ontology_item: object) -> str:
    """Return a readable display name for ontology properties/classes."""
    for attr in ("prefLabel", "label"):
        if hasattr(ontology_item, attr):
            text = _first_value_text(getattr(ontology_item, attr))
            if text:
                return text

    for attr in ("python_name", "name"):
        value = getattr(ontology_item, attr, None)
        if value:
            return str(value)

    return str(ontology_item)


def _render_value(value: object) -> str:
    """Render an ontology value as escaped HTML, linking URLs and ontology terms."""
    iri = getattr(value, "iri", None)
    if iri:
        label = html.escape(_display_name(value))
        iri_text = html.escape(str(iri), quote=True)
        return f'<a class="entity-popup__link" href="{iri_text}">{label}</a>'

    text = str(value).strip()
    if not text:
        return ""

    if text.startswith(("http://", "https://")):
        iri_text = html.escape(text, quote=True)
        label = html.escape(text)
        return f'<a class="entity-popup__link" href="{iri_text}">{label}</a>'

    return html.escape(text)


def _normalized_text(value: object) -> str:
    """Return a normalized text form for duplicate detection."""
    return " ".join(str(value).split())


def _popup_rows(entity: Entity) -> list[tuple[str, list[object]]]:
    """Collect all available ontology metadata rows for popup rendering."""
    ontology = entity.ontology
    rows: defaultdict[str, list[object]] = defaultdict(list)

    for prop in ontology.get_class_properties():
        try:
            values = list(prop[ontology])
        except Exception:  # noqa: BLE001
            # Some ontology properties cannot be evaluated for every
            # class; skip them silently so the popup still renders.
            continue
        values = [value for value in values if str(value).strip()]
        if not values:
            continue
        rows[_display_name(prop)].extend(values)

    if ontology.is_a:
        rows.setdefault("is_a", [])
        rows["is_a"].extend(ontology.is_a)

    names_by_lower = {name.lower(): name for name in rows}
    comment_name = names_by_lower.get("comment")
    elucidation_name = names_by_lower.get("elucidation")
    if comment_name and elucidation_name:
        elucidation_texts = {
            text
            for value in rows[elucidation_name]
            if (text := _normalized_text(value))
        }

        filtered_comment_values = [
            value
            for value in rows[comment_name]
            if (text := _normalized_text(value)) and text not in elucidation_texts
        ]
        if filtered_comment_values:
            rows[comment_name] = filtered_comment_values
        else:
            rows.pop(comment_name, None)

    preferred_order = [
        "definition",
        "elucidation",
        "comment",
        "example",
        "prefLabel",
        "altLabel",
        "isDefinedBy",
        "hasMeasurementUnit",
        "wikipediaReference",
        "wikidataReference",
        "qudtReference",
        "iupacReference",
        "is_a",
    ]
    preferred_names = {
        key.lower(): index for index, key in enumerate(preferred_order, start=1)
    }

    def sort_key(item: tuple[str, list[object]]) -> tuple[int, str]:
        name = item[0]
        return preferred_names.get(name.lower(), len(preferred_order) + 1), name.lower()

    return sorted(rows.items(), key=sort_key)


def _popup_html(entity: Entity) -> str:
    """Build HTML for a detailed ontology metadata popup."""
    rows_html: list[str] = []
    for name, values in _popup_rows(entity):
        rendered_values = [item for value in values if (item := _render_value(value))]
        if not rendered_values:
            continue

        if len(rendered_values) == 1:
            content = rendered_values[0]
        else:
            content = "".join(f"<li>{item}</li>" for item in rendered_values)
            content = f'<ul class="entity-tip__list">{content}</ul>'

        rows_html.append(f"<dt>{html.escape(name)}</dt><dd>{content}</dd>")

    label = html.escape(entity.ontology_label)
    iri = html.escape(entity.ontology_iri, quote=True)

    return (
        '<div class="entity-tip">'
        f'<div class="entity-tip__title">{label}</div>'
        f'<a class="entity-tip__iri" href="{iri}" target="_blank"'
        ' rel="noopener noreferrer">'
        f"{iri}"
        "</a>"
        '<dl class="entity-tip__dl">'
        f'{"".join(rows_html)}'
        "</dl>"
        "</div>"
    )


def _json_for_inline_script(value: str) -> str:
    """Return JSON text safe for embedding inside a script element."""
    return json.dumps(value).replace("</", "<\\/")


def entity_role(  # noqa: PLR0913
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: dict | None = None,
    content: list[str] | None = None,
) -> tuple[list[nodes.Node], list[nodes.system_message]]:
    """Create a clickable ontology term with a metadata popup."""
    del role
    del content

    options = {} if options is None else dict(options)
    label = text.strip()
    try:
        entity = Entity(label)
    except Exception as exc:  # pragma: no cover - handled by docutils at build time
        message = inliner.reporter.error(
            f"Cannot resolve :entity: label {label!r}: {exc}",
            line=lineno,
        )
        problematic = inliner.problematic(rawtext, rawtext, message)
        return [problematic], [message]

    classes = list(options.pop("classes", []))
    classes.append("entity-ref")
    reference = nodes.inline(rawtext, "", classes=classes)
    reference["tabindex"] = 0
    reference += nodes.emphasis(text=entity.ontology_label)
    popup_payload = nodes.raw(
        "",
        (
            '<script type="application/json" class="entity-tip-data">'
            f"{_json_for_inline_script(_popup_html(entity))}"
            "</script>"
        ),
        format="html",
    )
    return [reference, popup_payload], []


def setup(app: Sphinx) -> dict[str, bool]:
    """Register the :entity: role."""
    app.add_role("entity", entity_role)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
