# Frequency-Based Curvature Detection - Validation Suite

**Paper:** "Frequency-Based Curvature Detection via Dynamic Comparisons"  
**Authors:** Carmen N. Wrede, Lino P. Casu, Bingsi  
**Tests:** 56/56 (100% pass rate)

---

## Overview

This repository contains the complete validation test suite for the paper "Frequency-Based Curvature Detection via Dynamic Comparisons". The tests validate:

1. **Core Equations (Eq. 1-5)** - Frequency comparison framework
2. **Loop Closure (I_ABC = 0)** - Non-integrability detection
3. **NSR/NGR Separation** - Removable vs non-removable contributions
4. **Experimental Validation** - Real data from GP-A, Galileo, GPS, etc.
5. **SSZ Integration** - Connection to Segmented Spacetime theory

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
| **Total** | **56** | **56** | **100%** |

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

- Python >= 3.8
- NumPy >= 1.20
- pytest >= 7.0

---

## License

Anti-Capitalist Software License v1.4

---

## Citation

```bibtex
@article{Wrede2025,
  author = {Wrede, Carmen N. and Casu, Lino P. and Bingsi},
  title = {Frequency-Based Curvature Detection via Dynamic Comparisons},
  year = {2025},
  note = {Validation: 56/56 tests (100\%)}
}
```

---

## Contact

- Carmen N. Wrede
- Lino P. Casu

**Repository:** https://github.com/error-wtf/frequency-curvature-validation
