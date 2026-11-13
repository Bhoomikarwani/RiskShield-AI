🛡️RiskShield AI: PayPal Merchant Credit & Fraud Guard

**RiskShield AI** is an intelligent risk-assessment middleware and merchant guard built for the **PayPal AI Hackathon**[cite: 1]. It combines binary classification machine learning (powered by a CreditWise pipeline) with an AI Copilot to evaluate real-time checkout signals, prevent chargeback fraud, and dynamically control PayPal Sandbox settlements.

---

## 🚀 Key Features

* **🛒 Real-Time Checkout Signal Analysis:** Evaluates critical risk indicators including order amount, buyer account age, previous chargebacks, address matching, and order velocity.
* **🤖 CreditWise ML & AI Copilot Reasoning:** Predicts default/fraud probabilities using classification logic and generates natural-language reasoning explaining why a transaction is flagged.
* **💳 PayPal Settlement Gatekeeper:** 
  * **Low/Medium Risk:** Automatically clears the order and unlocks the official PayPal Sandbox payment button.
  * **High Risk:** Instantly locks the checkout interface to protect merchants from potential chargeback losses.
* **📋 Live Merchant Audit Log:** Tracks historical transaction decisions in real-time.

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit (Python)
* **Risk Engine:** Custom ML Classification Logic (adapted from the CreditWise pipeline)
* **Payment Integration:** PayPal Developer Sandbox APIs / Checkout SDK
* **State Management:** Streamlit Session State & Interactive Components

---
