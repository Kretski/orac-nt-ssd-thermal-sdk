import sys
import os
import time

# Добавяме пътя към главната директория, за да може Python да намери папката sdk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Опит за зареждане на ORAC API
try:
    from sdk.api import compute_vitality
    CORE_TYPE = "Pure Python (Evaluation Mode)"
except ImportError:
    print("❌ Error: SDK API not found. Ensure sdk/api.py exists.")
    sys.exit(1)

def run_ssd_demo():
    print("=" * 60)
    print("  ORAC-NT v5.5 — SSD Thermal Management SDK Demo")
    print(f"  Core Engine: {CORE_TYPE}")
    print("=" * 60)
    print(f"{'Step':<6} | {'NAND Temp':<10} | {'Quality Q':<10} | {'W Vitality':<10} | {'Status'}")
    print("-" * 60)

    # Симулирани данни за тест (Temp, NAND Quality Q, Performance D)
    # Тези данни в реалния контролер на Marvell идват от SMART/Telemetry
    simulation_data = [
        {"temp": 42.5, "Q": 0.98, "D": 1.0}, # Оптимално състояние
        {"temp": 59.2, "Q": 0.95, "D": 1.0}, # Навлизане в Onset зона (58C+)
        {"temp": 64.8, "Q": 0.88, "D": 0.9}, # Активно регулиране
        {"temp": 69.5, "Q": 0.75, "D": 0.7}, # Близо до Hard Limit (70C)
        {"temp": 72.1, "Q": 0.62, "D": 0.5}, # Survival Mode / Throttling
    ]

    T_onset = 58.0
    T_throttle = 70.0
    T_window = T_throttle - T_onset

    for i, data in enumerate(simulation_data):
        # 1. Изчисляваме нормализирания термичен стрес (T_norm)
        T_norm = max(0.0, (data['temp'] - T_onset) / T_window)
        
        # 2. ИЗВИКВАМЕ ORAC-NT CORE (W = Q*D - T_norm)
        W = compute_vitality(data['Q'], data['D'], T_norm)
        
        # 3. Определяне на статус
        status = "✅ STABLE" if W > 0 else "⚠️ SURVIVAL"
        
        print(f"{i+1:<6} | {data['temp']:<10.1f} | {data['Q']:<10.2f} | {W:<10.3f} | {status}")
        time.sleep(0.1)

    print("-" * 60)
    print("📝 RESULT: W(t) output allows for proportional micro-adjustments")
    print("   of the PCIe Gen4 clock speed to prevent NAND degradation.")
    print("=" * 60)

if __name__ == "__main__":
    run_ssd_demo()