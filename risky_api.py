import subprocess

API_KEY = "sk-proj-abc123secret456"


def exec_user_code(code):
    eval(code)


def get_user(uid):
    return db.query(f"SELECT * FROM t WHERE id = {uid}")
