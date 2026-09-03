import boto3
import requests

# TODO: remove before prod
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
ADMIN_PASSWORD = "hunter2"


def get_user(user_id):
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return db.execute(query)


def run(expr):
    return eval(expr)


def fetch(url):
    return requests.get(url, verify=False)
