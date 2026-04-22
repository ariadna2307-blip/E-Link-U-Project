# Reemplaza la parte de la tabla por esta:
if not df.empty:
    st.subheader("📍 Desglose de Impacto por Nación")
    
    # Creamos una versión "estilizada"
    df_styled = df.sort_values(by='annual_loss_billion', ascending=False)
    
    # Formateamos los números para que se vean como moneda
    st.dataframe(
        df_styled.style.format({
            "annual_loss_billion": "€{:.2f}B",
            "rural_recovery_potential": "€{:.2f}B"
        }).background_gradient(cmap="Reds", subset=["annual_loss_billion"]),
        use_container_width=True
    )
    
    st.bar_chart(data=df, x='country_name', y='annual_loss_billion', color="#FF4B4B")
