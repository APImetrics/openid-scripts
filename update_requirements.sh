# Note you need to install pip-tools: pip install pip-tools
pip-compile --upgrade --output-file requirements.txt requirements.in
pip-sync requirements.txt
