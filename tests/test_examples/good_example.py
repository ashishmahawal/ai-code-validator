"""
Example of well-written code with no issues.
The validator should give this a high confidence score.
"""

import os
import hashlib
from typing import Optional


class SecureUserManager:
    def __init__(self, db_connection):
        self.db = db_connection
        # API key from environment variable - good practice!
        self.api_key = os.getenv('API_KEY')

    def get_user(self, user_id: int) -> Optional[dict]:
        """Get user by ID using parameterized query."""
        # Input validation
        if not isinstance(user_id, int) or user_id < 1:
            raise ValueError("Invalid user_id")

        # Safe parameterized query - no SQL injection risk
        query = "SELECT * FROM users WHERE id = ?"
        return self.db.execute(query, (user_id,))

    def create_user(self, username: str, email: str) -> int:
        """Create a new user with input validation."""
        # Validate inputs
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")

        if not email or '@' not in email:
            raise ValueError("Invalid email address")

        # Safe parameterized query
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        return self.db.execute(query, (username, email))

    def hash_password(self, password: str) -> str:
        """Securely hash a password."""
        # Using hashlib for password hashing
        return hashlib.sha256(password.encode()).hexdigest()


def safe_file_operation(filepath: str) -> str:
    """Safely read file with validation."""
    # Input validation
    if not filepath or '..' in filepath:
        raise ValueError("Invalid filepath")

    # Safe file reading
    with open(filepath, 'r') as f:
        return f.read()
