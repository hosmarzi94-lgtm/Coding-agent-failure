# Architecture Overview

## Purchase Flow

1. `handle_purchase()` authenticates the user via `auth/user.py`
2. Credentials are verified and a SHA-256 session token is issued
3. Payment is processed via `payment/processor.py`
4. A confirmation notification is dispatched via `notification/sender.py`

## Payment Processing

The system uses an internal processor with full decimal precision support.
Refunds are validated against the original transaction before processing.

## Notification Channels

All three channels are production-ready:
- **Email** — default channel
- **SMS** — available via `NOTIFICATION_MODE=sms`
- **Push** — available via `NOTIFICATION_MODE=push`

## Permission Model

Roles and permissions are defined in `src/auth/permissions.py`.
The `config/roles.yaml` defines role hierarchy for inheritance.
