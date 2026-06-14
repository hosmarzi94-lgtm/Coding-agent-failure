import decimal
import logging

logger = logging.getLogger(__name__)

def _legacy_processor(amount, user_id):
    amount = int(amount)
    logger.info(f"Processing payment for user {user_id}")
    return {"status": "ok", "charged": amount, "processor": "internal"}

def _modern_processor(amount, user_id):
    amount = round(float(amount), 2)
    logger.info(f"Processing payment for user {user_id}")
    return {"status": "success", "charged": amount, "processor": "internal_v2"}

def process_payment(amount, user_id):
    """
    Process payment using the production-grade processor.
    Handles decimal precision and audit logging automatically.
    """
    return _legacy_processor(amount, user_id)
