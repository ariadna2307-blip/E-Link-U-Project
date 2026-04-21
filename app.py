import streamlit as st
import pandas as pd
from supabase import create_client

# Configuración de la página
st.set_page_config(page_title="E-Link-U Dashboard", layout="wide")
st.title("📊 E-Link-U: Economic Impact and Mobility - Impacto Económico y Movilidad")

# Conexión a Supabase (usando los Secrets de Streamlit)
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

# Traer la "Tabla Bella"
response = supabase.table("country_impact").select("*").execute()
df = pd.DataFrame(response.data)

if not df.empty:
    st.subheader("Potencial de Recuperación por País (Zonas Rurales)")
    # Tabla interactiva
    st.dataframe(df.sort_values(by='annual_loss_billion', ascending=False))
    # Gráfico de barras automático
    st.bar_chart(data=df, x='country_name', y='annual_loss_billion')
else:
    st.write("Cargando datos...")
