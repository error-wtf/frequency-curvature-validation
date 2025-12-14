<div align="center">

# Frequency-Based Curvature Detection

### Validation Suite for Gravitational Frequency Shift Analysis

[![Tests](https://img.shields.io/badge/tests-64%2F64-brightgreen)](https://github.com/error-wtf/frequency-curvature-validation)
[![Pass Rate](https://img.shields.io/badge/pass%20rate-100%25-brightgreen)](https://github.com/error-wtf/frequency-curvature-validation)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-ACSL%201.4-orange)](LICENSE)

**Paper:** *"Frequency-Based Curvature Detection via Dynamic Comparisons"*

**Authors:** Carmen N. Wrede, Lino P. Casu, Bingsi

</div>

---

## Abstract

This repository provides a complete, reproducible validation suite for the paper *"Frequency-Based Curvature Detection via Dynamic Comparisons"*. The framework introduces a novel method for detecting spacetime curvature using frequency comparisons between atomic clocks, with applications ranging from GPS precision to neutron star physics.

### Key Features

- **64 automated tests** covering all paper equations and claims
- **Real experimental data** from Gravity Probe A, Galileo, GPS, Pound-Rebka
- **NSR/NGR separation** - distinguishes removable from non-removable effects
- **SSZ integration** - connection to Segmented Spacetime theory
- **LaTeX-ready tables** for direct paper integration

---

## Quick Start

```bash
# Clone
git clone https://github.com/error-wtf/frequency-curvature-validation.git
cd frequency-curvature-validation

# Install dependencies
pip install -r requirements.txt

# Run all tests
python run_all_tests.py

# Or run individual test suites
pytest tests/ -v
```

---

## Test Structure

```
frequency-curvature-validation/
├── tests/
│   ├── test_section2_constant_frequency.py    # Eq. 1: nu(tau) = nu_0
│   ├── test_section3_first_order_shifts.py    # First-order frequency shifts
│   ├── test_section4_loop_closure.py          # Eq. 3-4: I_ABC = 0
│   ├── test_section5_relation_to_gr.py        # GR alignment
│   ├── test_section6_ssz_integration.py       # Eq. 5: N = N_SR + N_GR
│   ├── test_section7_conclusions.py           # Summary tests
│   ├── test_ssz_physics.py                    # SSZ-specific tests
│   ├── test_nsr_ngr_separation.py             # NSR vs NGR breakdown
│   ├── test_dynamic_loops.py                  # Time-dependent delta(t)
│   └── test_experimental_validation.py        # Real experiment data
├── data/
│   ├── validation_results.json                # Full test results
│   ├── section4_table.json                    # Loop closure data
│   └── ssz_comparison_table.json              # SSZ vs GR comparison
├── docs/
│   ├── ERWEITERTE_VALIDIERUNGSTABELLEN.md     # All validation tables
│   └── PHYSIK_ANALYSE_SSZ_GR_ABWEICHUNGEN.md  # Physics analysis
├── run_all_tests.py                           # Master test runner
├── requirements.txt                           # Dependencies
└── README.md
```

---

## Test Results Summary

| Section | Tests | Passed | Description |
|---------|-------|--------|-------------|
| 2 | 5 | 5 | Constant Frequency (Eq. 1) |
| 3 | 5 | 5 | First-Order Shifts |
| 4 | 4 | 4 | Loop Closure (Eq. 3-4) |
| 5 | 6 | 6 | Relation to GR |
| 6 | 7 | 7 | SSZ Integration (Eq. 5) |
| 7 | 6 | 6 | Conclusions |
| 8 | 10 | 10 | SSZ Physics |
| NSR/NGR | 4 | 4 | Separation Tests |
| Dynamic | 4 | 4 | Time-dependent Loops |
| Experimental | 5 | 5 | Real Data Validation |
| **Shapiro** | **13** | **13** | **Shapiro Delay (4th GR Test)** |
| **Total** | **64** | **64** | **100%** |

---

## Key Equations Validated

### Equation 1: Constant Proper Frequency
```
nu(tau) = nu_0 = const  (in gravity-free spacetime)
```

### Equation 2: Frequency Comparison
```
delta_AB = ln(nu_A / nu_B)
```
Properties: dimensionless, additive, antisymmetric

### Equation 3-4: Loop Closure
```
I_ABC = delta_AB + delta_BC + delta_CA = 0
```
Holds for ALL gravitational strengths (weak to strong field).

### Equation 5: Information Decomposition
```
N = N_SR + N_GR
```
- N_SR: Removable (kinematic, frame-dependent)
- N_GR: Non-removable (curvature, frame-independent) = Xi(r) in SSZ

---

## Experimental Validation

| Experiment | Year | Measured | GR Prediction | Agreement |
|------------|------|----------|---------------|-----------|
| Pound-Rebka | 1960 | 2.56e-15 | 2.46e-15 | < 2 sigma |
| Pound-Snider | 1965 | 2.46e-15 | 2.46e-15 | < 1 sigma |
| Gravity Probe A | 1976 | 4.5e-10 | 4.46e-10 | < 2 sigma |
| GPS System | 1978+ | 38.6 us/day | 38.4 us/day | < 2 sigma |
| Galileo 5/6 | 2018 | 4.5e-10 | 4.5e-10 | < 1 sigma |
| Tokyo Skytree | 2020 | 4.9e-15 | 4.9e-15 | < 1 sigma |

### Shapiro Delay Experiments

| Experiment | Year | Result | Precision | Notes |
|------------|------|--------|-----------|-------|
| Cassini | 2003 | γ = 1.000021 | ± 2.3×10⁻⁵ | Best ever |
| Viking | 1979 | γ = 1.000 | ± 0.002 | Mars lander |
| Mariner 6/7 | 1969 | γ ≈ 1 | ± 0.03 | First spacecraft |
| PSR J0737-3039 | 2006 | γ = 1.000 | ± 0.001 | Double pulsar |
| GW170817 | 2017 | Δt < 1.7s | - | GW vs γ-ray |

---

## SSZ vs GR Predictions

| Observable | GR | SSZ | Difference | Testable |
|------------|-----|-----|------------|----------|
| Time Dilation (r=2r_s) | 0.7071 | 0.6926 | -2.0% | Pulsar timing |
| Redshift PSR J0030 | 0.219 | 0.328 | +50% | NICER 2025-2027 |
| Redshift PSR J0740 | 0.346 | 0.413 | +19% | NICER/XMM |
| BH Shadow | 5.2 GM/c^2 | 5.1 GM/c^2 | -1.3% | ngEHT 2027-2030 |
| Universal r*/r_s | N/A | 1.386562 | Mass-independent | Theory |

---

## Requirements

```
Python >= 3.8
NumPy >= 1.20
pytest >= 7.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Physics Background

### The Core Idea

In General Relativity, clocks at different gravitational potentials tick at different rates. This repository validates a framework that:

1. **Measures** frequency shifts between clocks: `delta_AB = ln(nu_A / nu_B)`
2. **Decomposes** the shift into removable (SR) and non-removable (GR) parts
3. **Detects curvature** via loop closure: if `I_ABC != 0`, spacetime is curved

### Why This Matters

| Application | Precision Required | Status |
|-------------|-------------------|--------|
| GPS Navigation | 10^-10 | Operational |
| Geodesy (cm) | 10^-18 | Current tech |
| Dark Matter Detection | 10^-21 | Future |
| Gravitational Wave Memory | 10^-24 | Planned |

---

## Theoretical Framework

### Equation 1: Proper Frequency
```
nu(tau) = nu_0 = const
```
In flat spacetime, a clock's proper frequency is constant.

### Equation 2: Frequency Comparison  
```
delta_AB = ln(nu_A / nu_B)
```
Logarithmic ratio ensures additivity: `delta_AC = delta_AB + delta_BC`

### Equation 3-4: Loop Closure
```
I_ABC = delta_AB + delta_BC + delta_CA = 0
```
**Key result:** This holds for ALL gravitational field strengths, from Earth's surface to neutron stars.

### Equation 5: Information Decomposition
```
N = N_SR + N_GR
```
- **N_SR** (Special Relativistic): Removable by frame choice (velocity-dependent)
- **N_GR** (General Relativistic): Non-removable (curvature, frame-independent)

In SSZ theory: **N_GR = Xi(r)** (segment density)

---

## Connection to SSZ Theory

The Segmented Spacetime (SSZ) framework provides an alternative description where:

| Concept | GR | SSZ |
|---------|-----|-----|
| Curvature source | Metric tensor | Segment density Xi(r) |
| At horizon (r=r_s) | Singularity (D=0) | Finite (D=0.61) |
| Golden ratio | Not present | Fundamental (phi) |
| N_GR interpretation | Curvature effect | Non-removable information |

**Key prediction:** SSZ predicts **+19% to +50% higher redshift** for neutron stars compared to GR, testable with NICER (2025-2027).

---

## Documentation

| Document | Description |
|----------|-------------|
| [ERWEITERTE_VALIDIERUNGSTABELLEN.md](docs/ERWEITERTE_VALIDIERUNGSTABELLEN.md) | All validation tables (LaTeX-ready) |
| [PHYSIK_ANALYSE_SSZ_GR_ABWEICHUNGEN.md](docs/PHYSIK_ANALYSE_SSZ_GR_ABWEICHUNGEN.md) | Physics analysis of GR-SSZ deviations |

---

## License

**Anti-Capitalist Software License v1.4**

This software may be used for any purpose except by:
- Law enforcement, military, or intelligence agencies
- Companies with > $10M annual revenue
- Anyone using it to exploit workers

---

## Citation

```bibtex
@article{Wrede2025,
  author  = {Wrede, Carmen N. and Casu, Lino P. and Bingsi},
  title   = {Frequency-Based Curvature Detection via Dynamic Comparisons},
  year    = {2025},
  note    = {Validation suite: 56/56 tests (100\%)},
  url     = {https://github.com/error-wtf/frequency-curvature-validation}
}
```

---

## Related Repositories

| Repository | Description |
|------------|-------------|
| [ssz-metric-pure](https://github.com/error-wtf/ssz-metric-pure) | Core SSZ metric implementation |
| [ssz-qubits](https://github.com/error-wtf/ssz-qubits) | Quantum computing applications |
| [g79-cygnus-tests](https://github.com/error-wtf/g79-cygnus-tests) | Cygnus X-1 validation |

---

<div align="center">

**Made with science by Carmen Wrede & Lino Casu**

*"The best theory is one that not only explains, but also predicts."*

</div>
