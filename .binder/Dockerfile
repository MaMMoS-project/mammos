# ───────────────────────────────────────────────────────────────────
# 1) Base image: pick the SALOME community image + explicit tag
#
#    x86_64 example:
#      FROM trophime/salome:9.8.0-focal
#    ARM64 example:
#      FROM trophime/salome:9.13.0-UB24-arm64
# ───────────────────────────────────────────────────────────────────
FROM trophime/salome:9.14.0-debian12

###############################################################################
# 2) Become root – we’ll stay root only while installing software & fixing perms
###############################################################################
USER root

# --- discover the existing UID-1000 user ------------------------------------
# (Most SALOME community images create a user with uid 1000 already.)
RUN EXISTING_USER=$(getent passwd 1000 | cut -d: -f1) \
 && echo "Existing uid-1000 user is $EXISTING_USER" \
 && ln -s /home/$EXISTING_USER /home/jovyan

# Binder expects these env-vars:
ENV NB_USER=jovyan \
    NB_UID=1000 \
    HOME=/home/jovyan

# --- put SALOME on PATH ------------------------------------------------------
ENV SALOME_ROOT=/opt/SALOME-9.14.0-DB12
ENV PATH="${SALOME_ROOT}:${PATH}"

# ─── ensure login‐shells (e.g. Jupyter terminals) see SALOME on $PATH ───────
RUN printf 'export SALOME_ROOT=/opt/SALOME-9.14.0-DB12\nexport PATH="$SALOME_ROOT:$PATH"\n' \
    > /etc/profile.d/salome.sh
# ─────────────────────────────────────────────────────────────────────────────

###############################################################################
# 3) Create a tiny venv and install Jupyter (avoids PEP 668 “externally managed”)
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends python3-venv \
 && python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --upgrade pip \
 && /opt/venv/bin/pip install --no-cache-dir notebook jupyterlab jupyterhub ipykernel \
 && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:${PATH}"

###############################################################################
# 4) Copy the repo into $HOME and give uid 1000 ownership
###############################################################################
COPY . ${HOME}
RUN chown -R 1000:1000 ${HOME}

###############################################################################
# 5) Switch to uid 1000 and register the SALOME-Python kernel
###############################################################################
USER 1000
RUN python3 -m ipykernel install \
      --user \
      --name salome-py3 \
      --display-name "SALOME Python 3"

###############################################################################
# 6) Default command – Binder will append its own flags (port, token, /lab)
###############################################################################
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--NotebookApp.default_url=/lab/"]
