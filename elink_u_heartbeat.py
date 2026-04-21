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
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# --- EL DESGLOSE (Lo que lo hace profesional) ---
pop_eu = 450000000
loss_per_capita = 1020
total_loss = pop_eu * loss_per_capita

# Segmentación (Pruebas para tu discurso)
rural_impact = total_loss * 0.30 # 30% es población rural
migrant_impact = total_loss * 0.05 # 5% es impacto directo en migrantes

data_to_send = {
    "country_name": "EU Strategic Breakdown",
    "savings_recovery_euro": total_loss,
    "notes": f"Rural: {rural_impact}B | Migrant: {migrant_impact}B | Basis: €1020 per capita"
}

try:
    supabase.table("elink_u_simulations").insert(data_to_send).execute()
    print("¡Mambo detallado enviado!")
except Exception as e:
    print(f"Error: {e}")
