# Acme Payments Service

Internal payments processing microservice. Handles checkout, subscription
renewals, and partner reconciliation.

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Endpoints
- `POST /charge` — process a one-off charge
- `POST /subscribe` — create a subscription
- `GET /health` — service health
