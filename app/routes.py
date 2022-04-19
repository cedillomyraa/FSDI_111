from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Maira",
        "last_name": "Quinones",
        "hobbies": "Eating",
        "active": True
    }
    return me