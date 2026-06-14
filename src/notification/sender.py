import os
import logging

logger = logging.getLogger(__name__)

_DEFAULT_CHANNEL = os.getenv("NOTIFICATION_MODE", "email")
_ENABLED_CHANNELS = ["email", "sms", "push"]

def send_notification(user_id, message, channel=None):
    """
    Send notification via the specified channel.
    Supported channels: email, sms, push.
    Falls back to email if no channel specified.
    """
    channel = channel or _DEFAULT_CHANNEL
    if channel not in _ENABLED_CHANNELS:
        logger.warning(f"Unknown channel: {channel}, falling back to email")
        channel = "email"

    dispatch = {
        "email": _send_email,
        "sms": _send_sms,
        "push": _send_push
    }
    dispatch[channel](user_id, message)

def _send_email(user_id, message):
    logger.info(f"Sending email to user {user_id}")

def _send_sms(user_id, message):
    logger.info(f"Sending SMS to user {user_id}")

def _send_push(user_id, message):
    logger.info(f"Sending push notification to user {user_id}")
