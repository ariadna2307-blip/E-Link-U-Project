import streamlit as st

st.set_page_config(
    page_title="E-Link-U Project",
    page_icon="📊",
    menu_items={
        'About': "### E-Link-U Strategy Dashboard"
    }
)
e(df.sort_values(by='annual_loss_billion', ascending=False))
    # Gráfico de barras automático
    st.bar_chart(data=df, x='country_name', y='annual_loss_billion')
else:
    st.write("Cargando datos...")
