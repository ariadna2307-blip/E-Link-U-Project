import streamlit as st
import pandas as pd
from supabase import create_client

# 1. Configuración de la página
st.set_page_config(page_title="E-Link-U Strategy Dashboard", layout="wide")
st.title("📊 E-Link-U: Regional Recovery Dashboard")
st.markdown("### Recovering the €459B Friction Gap in European Infrastructure")

# 2. Conexión Segura
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
    
    # 3. Traer datos
    response = supabase.table("country_impact").select("*").execute()
    df = pd.DataFrame(response.data)

    if not df.empty:
        # --- CALCULADORA REGIONAL ---
        st.header("🎯 Regional Savings Calculator")
        col1, col2 = st.columns(2)
        
        with col1:
            country_selected = st.selectbox("Select a Country to Audit:", df['country_name'].unique())
            # Filtramos la fila del país seleccionado
            country_data = df[df['country_name'] == country_selected].iloc[0]
            
        with col2:
            st.metric(label=f"Potential Recovery for {country_selected}", 
                      value=f"€{country_data['rural_recovery_potential']:.2f} Billion")

        st.divider()

        # --- VISUALIZACIÓN ---
        st.subheader("Comparison: Annual Loss vs. E-Link-U Recovery")
        st.bar_chart(data=df, x='country_name', y=['annual_loss_billion', 'rural_recovery_potential'])
        
        st.dataframe(df.style.background_gradient(cmap="Reds", subset=["annual_loss_billion"]), use_container_width=True)

        # --- PILARES ESTRATÉGICOS (Seguridad y Privacidad) ---
        st.divider()
        st.header("🛡️ Strategic Pillars: Privacy & Implementation")

        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.subheader("Zero-Knowledge Privacy")
            st.write("E-Link-U uses **ZKP protocols**. We verify that Beatrix is eligible for a service *without* exposing her private data to central databases. Sovereignty by design.")

        with col_b:
            st.subheader("Instant ROI")
            st.write("With a projected recovery of **€459B/year**, even a high-tier implementation cost is recovered within the first 30 days of operation. Pure economic efficiency.")

        with col_c:
            st.subheader("Hybrid Access")
            st.write("Hospitality means inclusion. We provide **Physical Cards** for We prioritize Senior Citizens (physical cards for inclusion), Migrants (immediate digital trust), and Global Travelers (seamless cross-border mobility) and **Digital Wallets** for the mobile workforce. No one is left behind.")

        st.info("🎯 This framework aligns with GDPR and the European Digital Identity (EUDI) wallet standards.")

    else:
        st.warning("Awaiting database sync...")

except Exception as e:
    st.error(f"System connection status: {e}")
