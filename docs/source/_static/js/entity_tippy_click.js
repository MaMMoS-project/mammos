"use strict";

(function () {
    function getPayload(link) {
        const payload = link.nextElementSibling;
        if (!(payload instanceof HTMLScriptElement)) {
            return "";
        }
        if (!payload.classList.contains("entity-tip-data")) {
            return "";
        }
        if (payload.dataset.entityTipHtml) {
            return payload.dataset.entityTipHtml;
        }
        try {
            const html = JSON.parse(payload.textContent || '""');
            payload.dataset.entityTipHtml = html || "";
            return payload.dataset.entityTipHtml;
        } catch {
            return "";
        }
    }

    var globalListenersAttached = false;

    function initEntityPopups() {
        if (typeof window.tippy !== "function") {
            return;
        }

        let openInstance = null;
        const links = document.querySelectorAll(".entity-ref");

        links.forEach((link) => {
            if (link.dataset.entityPopupInit === "1") {
                return;
            }
            link.dataset.entityPopupInit = "1";
            const html = getPayload(link);
            if (!html) {
                return;
            }

            window.tippy(link, {
                content: html,
                allowHTML: true,
                interactive: true,
                appendTo: () => document.body,
                trigger: "mouseenter focus",
                placement: "bottom-start",
                delay: [250, 0],
                arrow: false,
                theme: "mammos-entity",
                maxWidth: 720,
                onShow(currentInstance) {
                    if (openInstance === currentInstance && currentInstance.state.isVisible) {
                        return false;
                    }
                    if (openInstance && openInstance !== currentInstance) {
                        openInstance.hide();
                    }
                    openInstance = currentInstance;
                    return true;
                },
                onHide(currentInstance) {
                    if (openInstance === currentInstance) {
                        openInstance = null;
                    }
                },
            });
        });

        if (!globalListenersAttached) {
            globalListenersAttached = true;

            document.addEventListener("pointerdown", (event) => {
                if (!openInstance) {
                    return;
                }
                const target = event.target;
                if (!(target instanceof Element)) {
                    return;
                }
                if (target.closest(".tippy-box")) {
                    return;
                }
                openInstance.hide();
            });

            document.addEventListener("keydown", (event) => {
                if (event.key === "Escape" && openInstance) {
                    openInstance.hide();
                }
            });
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initEntityPopups);
    } else {
        initEntityPopups();
    }
})();
