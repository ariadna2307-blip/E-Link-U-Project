import streamlit as st
import pandas as pd
from supabase import create_client

# 1. Page Config
st.set_page_config(page_title="E-Link-U Dashboard", layout="wide")
st.title("📊 E-Link-U: Economic Impact and Mobility - Impacto Económico y Movilidad ")

# 2. Connection (Check if secrets exist)
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    # 3. Fetch Data
    response = supabase.table("country_impact").select("*").execute()
    df = pd.DataFrame(response.data)

    # 4. Display Data (The part that was failing)
    if not df.empty:
        st.subheader("Recovery Potential by Country (Rural Areas) - Potencial de Recuperación por País (Zonas Rurales)")
        st.dataframe(df.sort_values(by='annual_loss_billion', ascending=False))
        st.bar_chart(data=df, x='country_name', y='annual_loss_billion')
    else:
        st.warning("La base de datos está conectada pero no se encontraron filas.")

except Exception as e:
    st.error(f"Error de conexión o configuración: {e}")
    st.info("Asegúrate de que SUPABASE_URL y SUPABASE_KEY estén en los 'Secrets' de Streamlit.")
