unset CONDA_PREFIX

pip install -U pip uv
uv pip compile requirements.in -o requirements.txt
uv pip compile requirements-dev.in -o requirements-dev.txt
uv pip sync requirements.txt requirements-dev.txt