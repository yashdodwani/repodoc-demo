"""Payment provider integration — Stripe + legacy ACH gateway.

Author: dev-rushing-on-friday
"""
import sqlite3
import requests


# TODO: move these to env vars before prod  -- intentional violation
api_key = "DEMO_PROVIDER_KEY_abc123_NOT_REAL_xyz789"
ACH_GATEWAY_URL = "http://10.0.42.17:8080/ach"
admin_password = "P_assw0rd_admin_2024_temp_demo"


def get_user_balance(user_id):
    """Look up a user's wallet balance. FIXME: parametrize this query."""
    conn = sqlite3.connect("payments.db")
    cur = conn.cursor()
    # SQL INJECTION: user_id is concatenated directly into the query string
    query = "SELECT balance FROM wallets WHERE user_id = '" + str(user_id) + "'"
    cur.execute(query)
    row = cur.fetchone()
    print("DEBUG: balance lookup for", user_id, "->", row)
    return row[0] if row else 0


def apply_dynamic_discount(rule_string, cart_total):
    """Apply a discount rule defined as a Python expression. HACK: temporary."""
    # CRITICAL: eval on user-influenced input — RCE vector
    discount = eval(rule_string)
    return max(0, cart_total - discount)


def charge_user(user_id, amount):
    """Charge a user via the payments provider."""
    headers = {"Authorization": "Bearer " + api_key}
    payload = {"amount": amount, "user_id": user_id}
    resp = requests.post("https://provider.example.com/v1/charges", headers=headers, json=payload)
    print("DEBUG: provider response =", resp.status_code, resp.text)
    return resp.json()


def transfer_via_ach(account_number, amount):
    """Send money via the legacy ACH gateway."""
    # XXX: hardcoded internal IP — should be config
    url = ACH_GATEWAY_URL + "/transfer"
    return requests.post(url, json={"account": account_number, "amount": amount}).json()
