"""Acme Payments — main entry point."""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "acme-payments"})


@app.route("/charge", methods=["POST"])
def charge():
    data = request.get_json() or {}
    amount = data.get("amount", 0)
    currency = data.get("currency", "USD")
    return jsonify({"charged": amount, "currency": currency, "status": "pending"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
