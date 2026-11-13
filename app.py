import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="RiskShield AI - PayPal Merchant Guard",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ RiskShield AI: PayPal Merchant Credit & Fraud Guard")
st.markdown("*Powered by CreditWise ML Binary Classification Engine & AI Copilot*")
st.divider()

# Layout in 3 Columns
col1, col2, col3 = st.columns(3)

# --- COLUMN 1: CHECKOUT SIGNALS ---
with col1:
    st.subheader("🛒 1. Checkout Signals")
    amount = st.number_input("Order Amount ($ USD)", value=450, step=10)
    account_age = st.number_input("Buyer Account Age (Days)", value=120, step=1)
    chargebacks = st.number_input("Previous Chargebacks", value=0, step=1)
    address_match = st.checkbox("Billing & Shipping Address Match", value=True)
    orders_24h = st.number_input("Orders in Last 24h", value=1, step=1)

    run_check = st.button("Run ML Risk Check", type="primary", use_container_width=True)

# --- COLUMN 2: ML MODEL & AI REASONING ---
with col2:
    st.subheader("🤖 2. AI Risk Assessment")
    
    if run_check:
        # Simulated ML Risk Scoring Logic (derived from CreditWise pipeline)
        risk_score = 15
        if amount > 1000: risk_score += 30
        if account_age < 15: risk_score += 25
        if chargebacks > 0: risk_score += chargebacks * 25
        if not address_match: risk_score += 20
        if orders_24h > 3: risk_score += 20
        
        risk_score = min(risk_score, 98)

        if risk_score >= 65:
            level = "HIGH"
        elif risk_score >= 35:
            level = "MEDIUM"
        else:
            level = "LOW"

        st.metric(label="Fraud / Chargeback Risk Probability", value=f"{risk_score}%")

        if level == "HIGH":
            st.error(f"**Risk Level: {level}** (Action: Block Settlement)")
        elif level == "MEDIUM":
            st.warning(f"**Risk Level: {level}** (Action: Review / 3D Secure)")
        else:
            st.success(f"**Risk Level: {level}** (Action: Auto-Approve)")

        st.markdown("**AI Copilot Reasoning:**")
        if level == "HIGH":
            st.write("- High chargeback probability detected based on buyer history.")
            st.write("- Account velocity anomaly flagged.")
        elif level == "MEDIUM":
            st.write("- Moderate transaction variance compared to baseline.")
        else:
            st.write("- Established buyer profile with verified address signals.")

        st.session_state["risk_level"] = level
        st.session_state["amount"] = amount
    else:
        st.info("👈 Enter checkout signals and click 'Run ML Risk Check'.")

# --- COLUMN 3: PAYPAL GATEKEEPER & SETTLEMENT ---
with col3:
    st.subheader("💳 3. PayPal Settlement Gate")
    
    if "risk_level" in st.session_state:
        level = st.session_state["risk_level"]
        amount = st.session_state["amount"]

        if level == "HIGH":
            st.error("🔒 **PayPal Checkout Locked**")
            st.write("Transaction blocked by RiskShield to protect merchant balance from potential chargeback fraud.")
        else:
            st.success(f"✓ **Cleared for PayPal Checkout (${amount} USD)**")
            
            # Sandbox simulation button linking to PayPal Sandbox Demo
            paypal_button_html = f"""
            <div style="background: #0070ba; padding: 12px; border-radius: 8px; text-align: center; cursor: pointer;">
                <a href="https://developer.paypal.com/demo/checkout/" target="_blank" style="color: white; font-weight: bold; text-decoration: none; font-size: 16px;">
                    Pay with PayPal (Sandbox)
                </a>
            </div>
            """
            st.markdown(paypal_button_html, unsafe_allow_html=True)
            st.caption("Clicking simulates secure PayPal sandbox settlement.")
    else:
        st.info("Awaiting risk classification...")

# Footer / Live Audit Logs
st.divider()
st.markdown("### 📋 Live Merchant Risk Audit Log")
st.code("""
[01:02:15] TXN-9841 | Amount: $450 | Risk: 15% (LOW)   -> Approved & Settled via PayPal Sandbox
[01:00:42] TXN-3312 | Amount: $2200| Risk: 85% (HIGH)  -> Blocked (Chargeback Guard Active)
[00:58:10] TXN-1092 | Amount: $120 | Risk: 10% (LOW)   -> Approved & Settled via PayPal Sandbox
""", language="text")