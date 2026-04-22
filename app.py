if not df.empty:
    st.subheader("Potencial de Recuperación por País (Zonas Rurales)")
    # Both lines below must start at the exact same vertical level
    st.dataframe(df.sort_values(by='annual_loss_billion', ascending=False))
    st.bar_chart(data=df, x='country_name', y='annual_loss_billion')
else:
    st.write("Cargando datos...")

