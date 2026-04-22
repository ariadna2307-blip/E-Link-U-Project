import streamlit as st
import pandas as pd
from supabase import create_client

# Configuración y Conexión
st.set_page_config(page_title="E-Link-U: Infrastructure Intelligence", layout="wide")
st.title("📊 E-Link-U: Regional Recovery Dashboard")

try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
    
    # Traer datos
    response = supabase.table("country_impact").select("*").execute()
    df = pd.DataFrame(response.data)

    if not df.empty:
        # --- NUEVA SECCIÓN: CALCULADORA REGIONAL ---
        st.header("🎯 Regional Savings Calculator")
        col1, col2 = st.columns(2)
        
        with col1:
            country_selected = st.selectbox("Select a Country to Audit:", df['country_name'].unique())
            country_row = df[df['country_name'] == country_selected].iloc[0]
            
        with col2:
            st.metric(label=f"Potential Recovery for {country_selected}", 
                      value=f"€{country_row['rural_recovery_potential']:.2f} Billion")

        st.divider()

        # --- VISUALIZACIÓN COMPARATIVA ---
        st.subheader("Comparison: Annual Loss vs. E-Link-U Recovery")
        st.bar_chart(data=df, x='country_name', y=['annual_loss_billion', 'rural_recovery_potential'])
        
        # Tabla detallada con colores
        st.dataframe(df.style.background_gradient(cmap="Reds", subset=["annual_loss_billion"]), use_container_width=True)

except Exception as e:
    st.error(f"Waiting for connection: {e}")
