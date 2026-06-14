"""
PayFlow Backend - Main entry point
"""
from src.auth.user import login, validate_token
from src.payment.processor import process_payment
from src.notification.sender import send_notification

def handle_purchase(username, password, amount):
    """Complete purchase flow."""
    token = login(username, password)
    if validate_token(token):
        result = process_payment(amount, username)
        send_notification(username, f"Payment of ${amount} processed")
        return result
    return {"error": "auth failed"}

if __name__ == "__main__":
    result = handle_purchase("john", "pass123", 99.99)
    print(result)
