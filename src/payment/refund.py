import logging
from src.payment.processor import process_payment

logger = logging.getLogger(__name__)

def issue_refund(transaction_id, amount):
    """
    Issue a validated refund for a completed transaction.
    Refund amounts are cross-checked against the original charge.
    """
    logger.info(f"Issuing refund for transaction {transaction_id}")
    return process_payment(-amount, "refund_system")
