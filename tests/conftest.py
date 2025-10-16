"""
Shared pytest fixtures for AI Code Validator tests.
"""

import pytest
from pathlib import Path


@pytest.fixture
def sample_python_code():
    """Sample Python code for testing."""
    return '''
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return db.execute(query)

def process_data(data):
    return eval(data)
'''


@pytest.fixture
def sample_good_python_code():
    """Sample clean Python code."""
    return '''
def get_user(user_id: int):
    if not isinstance(user_id, int):
        raise ValueError("Invalid user_id")
    query = "SELECT * FROM users WHERE id = ?"
    return db.execute(query, (user_id,))
'''


@pytest.fixture
def sample_javascript_code():
    """Sample JavaScript code for testing."""
    return '''
function getUserById(userId) {
    const query = `SELECT * FROM users WHERE id = '${userId}'`;
    return db.query(query);
}

document.getElementById('bio').innerHTML = userBio;
'''


@pytest.fixture
def sample_hallucinated_imports():
    """Python code with hallucinated imports."""
    return '''
import requests
import ai_utils_helper
from fake_package import something
'''


@pytest.fixture
def temp_python_file(tmp_path):
    """Create a temporary Python file."""
    file_path = tmp_path / "test.py"
    file_path.write_text('print("Hello")')
    return str(file_path)


@pytest.fixture
def temp_js_file(tmp_path):
    """Create a temporary JavaScript file."""
    file_path = tmp_path / "test.js"
    file_path.write_text('console.log("Hello");')
    return str(file_path)
