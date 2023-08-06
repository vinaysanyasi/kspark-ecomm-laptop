# kspark-ecomm-laptop
kspark-ecomm-laptop 

# create virtual environment
python -m venv .venv

# activate virtual environment (do it in cmd/powershell so we could see (.venv))
.venv/Scripts/activate

# install requirements.txt
pip install -r requirements.txt

# to run uvicorn server
uvicorn main:app --reload

