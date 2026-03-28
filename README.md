# ORAC-NT v5.5
### Orbital Resilience Adaptive Controller — Neural-Thermal Edition

> **Deterministic Physical AI for Ultra-Low-Power Embedded Systems**  
> *Replacing probabilistic neural networks with provably stable physics.*

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![Platform: STM32F4](https://img.shields.io/badge/Platform-STM32F4-blue.svg)]()
[![Validated: Hardware](https://img.shields.io/badge/Validated-Hardware%20%2B%20Simulation-green.svg)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18898599.svg)](https://doi.org/10.5281/zenodo.18898599)

![ORAC-NT Proof](https://github.com/user-attachments/assets/7b293f4f-ac91-4de4-9fbe-544050d0dee7)

---

## The Problem

Modern AI controllers for space, drones and industrial systems rely on neural networks that:
- Require **megabytes** of RAM and flash
- Consume **milliwatts** continuously — unacceptable for CubeSats and battery-powered devices
- Are **probabilistic** — no formal stability guarantees
- Show high disruption rates in critical regimes (plasma, vibration, Byzantine sensor faults)
-## The Hidden Cost of Neural AI

Many companies have already spent hundreds of thousands of euros (and some millions) developing neural controllers that:
- Never make it into production due to power budget
- Require constant retuning when conditions change
- Don't provide any formal guarantees of stability

ORAC-NT is not "just another optimizer".
It is a **physically deterministic** replacement that makes much of the existing AI efforts economically unviable. 
## The Solution: ORAC-NT

ORAC-NT replaces the entire neural stack with a **single deterministic physics equation**:

```c
W(t) = Q(t) · D(t) − T(t)

























SymbolMeaningQ(t)Signal quality from Byzantine-aware dual-sensor fusionD(t)Decision capability (available compute & power budget)T(t)Entropy/thermal cost (temperature + computational stress)W(t)Vitality index — positive = healthy operation
When W ≤ 0, the system automatically enters survival mode (adaptive freeze). This check can be implemented even with a simple analog comparator — zero CPU cycles in critical cases.

Hardware Benchmark (STM32F401 @ 84 MHz, 3.3V)



































MetricORAC-NTTinyML (16-node)ImprovementRAM16 bytes62,500 bytes~4,000× smallerLatency~35 ns—Sub-microsecondPower9.90 μW33.0 mW~3,334× lowerEnergy savedAdaptive freeze0%Up to 51.5%
Measured on real hardware using DWT cycle counter. 80,000 cycles validated.

Simulation Results (9,000 missions)



































TestDetection RateFalse AlarmsAvg LatencySilent Drift100%0~12 stepsByzantine Adversarial100%0~8 stepsCascading Failure100%0~6 stepsFinal Boss (all faults)100%0~9 steps

Architecture
textSensor A (0x68) ─┐
                 ├─► Byzantine Fusion → Q(t)
Sensor B (0x69) ─┘
                           ▼
                    W(t) = Q·D − T
                           ▼
               ┌───────────┴───────────┐
             W > 0                   W ≤ 0
          Normal Mode             Survival Mode
         (full operation)       (freeze + save energy)

Quick Start
C#include "orac_nt.h"

static OracNode_t node;                    // 16 bytes persistent state
static OracConfig_t cfg = orac_default_config();

void loop() {
    OracSensorInput_t input = { mag_A, mag_B, temp_C };
    
    OracStatus_t status;
    orac_fuse(&input, &status, baseline, range);   // Byzantine fusion

    uint32_t cycles = 0;
    bool active = orac_step(&node, &cfg, gradient, status.W, step, &cycles);
    
    // active == false → node is frozen (energy saved)
}

Repository Structure
textORAC-NT-Public/
├── orac_nt.h              ← Public API header
├── liborac_lib_final.a    ← Pre-compiled evaluation library (STM32F4)
├── main.c                 ← Example usage
├── LICENSE
├── README.md
└── results/
    └── orac_v54_proof.png
Note: The core implementation is proprietary and delivered as a static library for evaluation.
Full source code is available only under Developer Kit or Production license.

Licensing & Pricing

























TierAccessPriceEvaluationHeader + precompiled .a libraryFreeDeveloper KitFull source + documentation + 1 year support€500ProductionFull source + support + IP rights€25,000
For licensing inquiries: kretski1@gmail.com

Applications

🛰️ CubeSat attitude control and fault detection
🤖 Autonomous drones – Byzantine IMU fusion
🏭 Industrial IoT – long-life battery nodes
🚗 Automotive – deterministic ASIL-B compatible control
🔬 Medical implants – ultra-low power budget


Citation
bibtex@misc{orac_nt_2025,
  title  = {ORAC-NT: Deterministic Physical AI for Embedded Control},
  author = {Kretski},
  year   = {2025},
  doi    = {10.5281/zenodo.18898599},
  note   = {Patent pending}
}

Patent & IP Status

Digital priority established via Zenodo DOI
Core logic protected as trade secret in the static library
Journal submission under review (IEEE TAES, 2026)