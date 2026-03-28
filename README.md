# ORAC-NT v5.5 | SSD Thermal Management SDK
### Deterministic Vitality Control for Next-Gen NAND Reliability

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![NAND Endurance](https://img.shields.io/badge/Endurance-31.6%25%20Gain-green.svg)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19019599.svg)](https://doi.org/10.5281/zenodo.19019599)

## 📌 Overview
ORAC-NT (Orbital Resilience Adaptive Controller) is a physics-based control engine designed to replace binary thermal throttling in high-performance NVMe controllers. By implementing the **W(t) Vitality Index**, the SDK prevents performance "cliff-drops" and significantly extends NAND P/E cycle lifetime through deterministic FDIR (Fault Detection, Isolation, and Recovery) logic.

---

## 🔬 Scientific Foundation
This SDK is based on the research published in Zenodo:
**"ORAC-NT v5.x: Optimal and Stable FDIR Architecture for Autonomous Spacecraft and Critical Systems"**
- **DOI:** [10.5281/zenodo.19019599](https://doi.org/10.5281/zenodo.19019599)
- **Framework:** Control Lyapunov Function (CLF) formulation for system stability ($V < 0$).

---

## 🚀 Benchmark Results (NAND Stress Test)
Validated using an Arrhenius-based thermal acceleration model ($E_a = 0.65 eV$):

| Metric | Fixed Threshold | **ORAC-NT (W(t))** | **Improvement** |
| :--- | :--- | :--- | :--- |
| **NAND Lifetime** | 23,920 cycles | **16,353 cycles cost** | **+31.6% Longevity** |
| **Avg. Junction Temp** | 68.5°C | **62.9°C** | **-5.6°C Reduction** |
| **Bit Error Rate (BER)** | Baseline | **-6.1% Reduction** | **Higher Integrity** |
| **Throttle Events** | 411 (Hard Drops) | **1817 (Micro)** | **Proactive Stability** |

---

## 🧠 The Vitality Formula
The core logic replaces probabilistic AI with deterministic physics for sub-microsecond execution:
$$W(t) = Q(T) \cdot D(t) - T_{norm}(t)$$

- **Q(T)**: Real-time NAND read quality (Health metric).
- **D(t)**: Controller performance fraction.
- **T_norm**: Normalized thermal stress window.

---

## 📂 Repository Structure
- `sdk/`: Core Python API for mathematical validation.
- `examples/`: Demo simulation showing the thermal damping effect.
- `benchmarks/`: Raw data and visualization plots (PNG).
- `docs/`: Technical White Paper and Academic Reference.

---

## 🛠 Quick Start
```bash
# Clone the evaluation SDK
git clone [https://github.com/Kretski/orac-nt-ssd-thermal-sdk.git](https://github.com/Kretski/orac-nt-ssd-thermal-sdk.git)
cd orac-nt-ssd-thermal-sdk

# Run the thermal simulation demo
python examples/demo_simulation.py