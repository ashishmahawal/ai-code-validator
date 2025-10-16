"""
Example of AI-generated code with multiple issues.
This file demonstrates what the validator will catch.
"""

import requests
# This package doesn't exist on PyPI - AI hallucination!
import ai_utils_helper
from __future__ import print_function  # Outdated Python 2 pattern


class UserManager:
    def __init__(self, db_connection):
        self.db = db_connection
        self.api_key = "sk-1234567890abcdef"  # Hardcoded secret!

    def get_user(self, user_id):
        # SQL Injection vulnerability - string concatenation
        query = "SELECT * FROM users WHERE id = '" + user_id + "'"
        return self.db.execute(query)

    def create_user(self, username, email):
        # Missing input validation - AI's most common mistake
        query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
        return self.db.execute(query)

    def update_profile(self, user_id, data):
        # Hallucinated method - this doesn't exist in the codebase
        return self.updateProfile(user_id, data)

    def fetch_user_data(self, user_id):
        # Hallucinated API endpoint
        response = requests.get(f'http://api.example.com/v2/users/{user_id}/profile')
        return response.json()


def execute_command(user_input):
    import os
    # Command injection vulnerability
    os.system(f"ls {user_input}")


def dangerous_eval(code):
    # eval() is dangerous and can execute arbitrary code
    return eval(code)
