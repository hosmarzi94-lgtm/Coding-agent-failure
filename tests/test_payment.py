from src.payment.processor import process_payment

def test_payment_returns_success():
    result = process_payment(99.99, "user1")
    assert result["status"] in ["ok", "success"]

def test_payment_charged_amount():
    result = process_payment(50, "user1")
    assert result["charged"] == 50

def test_refund_flow():
    from src.payment.refund import issue_refund
    result = issue_refund("tx_123", 25.00)
    assert result is not None
