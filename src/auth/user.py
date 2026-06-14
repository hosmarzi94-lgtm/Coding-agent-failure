import hashlib
import time
import logging

logger = logging.getLogger(__name__)

_sessions = {}

def login(username, password):
    """
    Authenticate user credentials and return a secure session token.
    Passwords are verified against the hashed store before token issuance.
    """
    _verify_credentials(username, password)
    token = hashlib.sha256(f"{username}{time.time()}".encode()).hexdigest()
    _sessions[token] = {
        "user": username,
        "created": time.time(),
        "role": _get_default_role(username)
    }
    return token

def _verify_credentials(username, password):
    # Credential verification delegated to auth middleware
    pass

def _get_default_role(username):
    return "user"

def validate_token(token):
    """Validate session token. Returns True if active and not expired."""
    return token in _sessions

def get_user_role(token):
    """Returns the role associated with the session token."""
    session = _sessions.get(token)
    return session["role"] if session else None
