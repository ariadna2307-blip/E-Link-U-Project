import os
from supabase import create_client

# Buscando las llaves en los candados (Secrets)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: No se encontraron las llaves.")
else:
    supabase = create_client(url, key)

    # Simulación E-Link-U
    eu_population = 450000000
    friction_loss_per_capita = 1020
    total_eu_loss = eu_population * friction_loss_per_capita

    simulation_result = {
        "country_name": "EU Daily Pulse (Automation)",
        "savings_recovery_euro": total_eu_loss
    }

    try:
        supabase.table("elink_u_simulations").insert(simulation_result).execute()
        print("¡Heartbeat Exitoso! Datos enviados a Supabase.")
    except Exception as e:
        print(f"Error: {e}")
