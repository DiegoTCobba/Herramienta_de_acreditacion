import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000"

st.title("💸 Sistema de Operaciones")

# --- SIDEBAR ---
st.sidebar.header("Credenciales API")
api_user = st.sidebar.text_input("Usuario")
api_pass = st.sidebar.text_input("Password", type="password")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["Crédito", "Débito", "TIN"])

# -------------------------
# CRÉDITO
# -------------------------
with tab1:
    st.subheader("Acreditación")

    account_id = st.text_input("Account ID")
    currency = st.selectbox("Moneda", ["PEN", "USD"])
    amount = st.text_input("Monto")

    if st.button("Ejecutar Crédito"):
        data = {
            "account_id": account_id,
            "currency": currency,
            "amount": amount,
            "description": "DEPOSITO",
            "user": api_user,
            "password": api_pass,
            "url": "https://q6caqnpy09.execute-api.us-east-1.amazonaws.com/OPS/kpayout/v1/psp_operations"
        }

        r = requests.post(f"{API_URL}/credit", json=data)
        st.json(r.json())

# -------------------------
# DÉBITO
# -------------------------
with tab2:
    st.subheader("Débito")

    account_id = st.text_input("Account ID ", key="deb")
    currency = st.selectbox("Moneda ", ["PEN", "USD"], key="deb_cur")
    amount = st.text_input("Monto ", key="deb_amt")

    if st.button("Ejecutar Débito"):
        data = {
            "account_id": account_id,
            "currency": currency,
            "amount": amount,
            "description": "AJUSTE",
            "user": api_user,
            "password": api_pass,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "url": "https://q6caqnpy09.execute-api.us-east-1.amazonaws.com/OPS/kpayout/v1/withdrawal_process"
        }

        r = requests.post(f"{API_URL}/debit", json=data)
        st.json(r.json())

# -------------------------
# TIN
# -------------------------
with tab3:
    st.subheader("Extractor TIN")

    texto = st.text_area("Pega texto o PDF parseado")

    if st.button("Extraer TINs"):
        r = requests.post(f"{API_URL}/tin", json={"texto": texto})
        st.json(r.json())
