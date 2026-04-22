# Reemplaza la parte de la tabla por esta:
import streamlit as st
import pandas as pd
from supabase import create_client

# 1. Configuración de la página
st.set_page_config(page_title="E-Link-U Dashboard", layout="wide")
st.title("📊 E-Link-U: Economic Impact and Mobility - Impacto Económico y Movilidad")
st.markdown("### Recuperando la eficiencia para ciudadanos como Beatrix")

# 2. Conexión Segura
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    # 3. Traer los datos de la tabla country_impact
    response = supabase.table("country_impact").select("*").execute()
    df = pd.DataFrame(response.data)

    # 4. Diseño y Visualización
    if not df.empty:
        st.subheader("📍Impact Breakdown by Nation - Desglose de Impacto por Nación")
        
        # Ordenar y formatear la tabla con colores
        df_styled = df.sort_values(by='annual_loss_billion', ascending=False)
        
        # Aplicamos el diseño: Moneda (€) y degradado de color rojo
        st.dataframe(
            df_styled.style.format({
                "annual_loss_billion": "€{:.2f}B",
                "rural_recovery_potential": "€{:.2f}B"
            }).background_gradient(cmap="Reds", subset=["annual_loss_billion"]),
            use_container_width=True
        )
        
        # Gráfico de barras con un color sólido profesional
        st.bar_chart(data=df, x='country_name', y='annual_loss_billion', color="#FF4B4B")
        
    else:
        st.warning("La base de datos está conectada pero no hay datos aún.")

except Exception as e:
    st.error(f"Error de conexión: {e}")
