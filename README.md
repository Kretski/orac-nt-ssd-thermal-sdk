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
- Consume **milliwatts** continuously — catastrophic for CubeSats
- Are **probabilistic** — no formal stability guarantees
- Show up to **27% disruption rates** in critical regimes (plasma, hypersonic)

## The Hidden Cost of Neural AI

Many companies have already spent hundreds of thousands of euros (some millions) developing neural controllers that:
- Never reach production due to power budget
- Require constant retuning when conditions change
- Provide no formal stability guarantees

ORAC-NT is not “just another optimizer”. It is a **physically deterministic** replacement that makes a large part of existing AI efforts economically unviable.

---

## The Solution: ORAC-NT

ORAC-NT replaces the neural stack with a **single deterministic physics equation**:

```c
W(t) = Q(t) · D(t) − T(t)
Symbol	Meaning
Q(t)	Signal quality from Byzantine-aware dual-sensor fusion
D(t)	Decision capability (available compute & power budget)
T(t)	Entropy/thermal cost (temperature + computational stress)
W(t)	Vitality index — positive = healthy operation
When W ≤ 0, the system automatically enters survival mode (adaptive freeze). This check can even be done with a simple analog comparator — zero CPU cycles.
________________________________________
Hardware Benchmark (STM32F401 @ 84 MHz, 3.3V)
Metric	ORAC-NT	TinyML (16-node)	Improvement
RAM	16 bytes	62,500 bytes	~4,000× smaller
Latency	~35 ns	—	Sub-microsecond
Power	9.90 μW	33.0 mW	~3,334× lower
Energy saved	Adaptive freeze	0%	Up to 51.5%
Measured on real hardware using DWT cycle counter.
________________________________________
Simulation Results (9,000 missions)
Test	Detection Rate	False Alarms	Avg Latency
Silent Drift	100%	0	~12 steps
Byzantine Adversarial	100%	0	~8 steps
Cascading Failure	100%	0	~6 steps
Final Boss (all faults)	100%	0	~9 steps
________________________________________
Quick Start
C
#include "orac_nt.h"

static OracNode_t node;                    // 16 bytes persistent state
static OracConfig_t cfg = orac_default_config();

void loop() {
    OracSensorInput_t input = { mag_A, mag_B, temp_C };
    
    OracStatus_t status;
    orac_fuse(&input, &status, baseline, range);

    uint32_t cycles = 0;
    bool active = orac_step(&node, &cfg, gradient, status.W, step, &cycles);
    
    // active == false → frozen (energy saved)
}
________________________________________
Repository Structure
text
ORAC-NT-Public/
├── orac_nt.h              ← Public API header
├── liborac_lib_final.a    ← Pre-compiled evaluation library
├── main.c                 ← Example
├── LICENSE
├── README.md
└── results/
    └── orac_v54_proof.png
Note: Core implementation is proprietary (delivered as static library). Full source available under paid licenses.
________________________________________
Licensing & Pricing
Tier	Access	Price
Evaluation	Header + .a library	Free
Developer Kit	Full source + docs + 1 year support	€500
Production	Full source + support + IP rights	€25,000
For licensing: kretski1@gmail.com

