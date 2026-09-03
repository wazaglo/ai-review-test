import os
import subprocess
import hashlib

AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "hunter2"


def run_command(user_input):
    os.system("echo " + user_input)


def login(user, password):
    query = "SELECT * FROM users WHERE name='%s' AND pw='%s'" % (user, password)
    return query


def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()


def read_file(path):
    return open("/etc/" + path).read()
