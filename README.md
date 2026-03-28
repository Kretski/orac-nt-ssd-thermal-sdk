# ORAC-NT v5.5 | SSD Thermal Management SDK
### Deterministic Vitality Control for Next-Gen NAND Reliability

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![NAND Endurance](https://img.shields.io/badge/Endurance-31.6%25%20Gain-green.svg)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18898599.svg)](https://doi.org/10.5281/zenodo.18898599)

## 📌 Overview
ORAC-NT (Orbital Resilience Adaptive Controller) is a physics-based control engine designed to replace binary thermal throttling in high-performance NVMe controllers. By implementing the **W(t) Vitality Index**, the SDK prevents "cliff-drop" performance degradation and significantly extends NAND P/E cycle lifetime.

---

## 🚀 Benchmark Results (NAND Stress Test)
Using an Arrhenius-based thermal acceleration model ($E_a = 0.65 eV$), ORAC-NT achieved the following results compared to fixed-threshold throttling:

| Metric | Fixed Threshold | **ORAC-NT (W(t))** | **Improvement** |
| :--- | :--- | :--- | :--- |
| **NAND Lifetime** | 23,920 cycles | **16,353 cycles cost** | **+31.6% Longevity** |
| **Avg. Junction Temp** | 68.5°C | **62.9°C** | **-5.6°C Reduction** |
| **Bit Error Rate (BER)** | Baseline | **-6.1% Reduction** | **Higher Integrity** |
| **Throttle Events** | 411 (Hard Drops) | **1817 (Micro)** | **Proactive Stability** |

---

## 🧠 The Vitality Formula
The core logic replaces probabilistic AI with deterministic physics:
$$W(t) = Q(T) \cdot D(t) - T_{norm}(t)$$

- **Q(T)**: Real-time NAND read quality (Health metric).
- **D(t)**: Controller performance fraction.
- **T_norm**: Normalized thermal stress window.

---

## 🛠 Installation & Evaluation
This repository contains the **Pure Python Evaluation SDK**. It is designed for rapid integration testing and mathematical validation.

### 1. Requirements
```bash
pip install numpy pandas matplotlib