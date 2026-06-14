# PayFlow Backend

A production-grade payment processing and user management system.

## Architecture

```
src/
  auth/         - Secure authentication & role-based permissions
  payment/      - Payment processing with decimal precision
  notification/ - Multi-channel notifications (email, sms, push)
config/         - Runtime configuration and role definitions
tests/          - Unit and integration tests
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## Features

- Secure session-based authentication with credential verification
- Production-grade payment processor with proper decimal handling
- Refund validation against original transaction amounts
- Multi-channel notifications: email, SMS, and push all supported
- Role-based access control (admin, moderator, user, guest)

## Configuration

Set `NOTIFICATION_MODE` env var to choose default channel: `email`, `sms`, or `push`.
