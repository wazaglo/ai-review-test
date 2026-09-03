from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def users():
    return {"users": ["alice", "bob"]}
