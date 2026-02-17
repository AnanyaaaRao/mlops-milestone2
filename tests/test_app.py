import sys
sys.path.append("app")

from app import app

def test_root_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running!", 200


