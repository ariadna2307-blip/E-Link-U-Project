import os
from supabase import create_client

# El 'cerebro' busca las llaves en los candados de seguridad (Secrets)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: No se encontraron las llaves de Supabase. Revisa los Secrets.")
else:
    supabase = create_client(url, key)

    # La lógica de tu proyecto E-Link-U
    eu_population = 450000000
    friction_loss_per_capita = 1020
    total_eu_loss = eu_population * friction_loss_per_capita

    # Datos para guardar en la 'Memoria' (Supabase)
    simulation_result = {
        "country_name": "EU Daily Pulse (Automation)",
        "savings_recovery_euro": total_eu_loss
    }

    try:
        supabase.table("elink_u_simulations").insert(simulation_result).execute()
        print("¡Heartbeat Exitoso! Datos de la UE enviados a Supabase automáticamente.")
    except Exception as e:
        print(f"Error al enviar datos: {e}")
