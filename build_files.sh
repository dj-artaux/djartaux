# build_files.sh
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
python3.9 manage.py collectstatic
