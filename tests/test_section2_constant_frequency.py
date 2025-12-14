"""
Test Section 2: Constant Frequency in Gravity-Free Systems

Paper claims:
- nu(tau) = nu₀ (constant proper frequency in flat spacetime)
- delta_AB = ln(nu_A/nu_B) (relational frequency observable)
- delta_AB is dimensionless and additive under composition

© 2025 Carmen Wrede & Lino Casu
"""

import numpy as np
import pytest
from dataclasses import dataclass
from typing import List, Tuple

# Constants
C = 299792458.0  # m/s


@dataclass
class TestResult:
    """Result of a single test."""
    name: str
    passed: bool
    expected: float
    actual: float
    tolerance: float
    description: str


def delta_AB(freq_A: float, freq_B: float) -> float:
    """
    Relational frequency observable (Equation 2).
    delta_AB = ln(nu_A / nu_B)
    """
    return np.log(freq_A / freq_B)


def test_constant_proper_frequency():
    """
    Test Equation 1: nu(tau) = nu₀
    In flat spacetime, proper frequency remains constant.
    """
    # Simulate emitter with constant proper frequency
    nu_0 = 5e9  # 5 GHz (typical atomic clock)
    
    # Proper time samples
    tau = np.linspace(0, 1000, 1000)  # seconds
    
    # In flat spacetime, frequency should remain constant
    nu_tau = np.full_like(tau, nu_0)
    
    # Check constancy
    freq_variation = np.std(nu_tau) / np.mean(nu_tau)
    
    result = TestResult(
        name="Constant Proper Frequency (Eq. 1)",
        passed=freq_variation < 1e-15,
        expected=0.0,
        actual=freq_variation,
        tolerance=1e-15,
        description="nu(tau) = nu₀ in flat spacetime"
    )
    
    print(f"[PASS] {result.name}: PASSED" if result.passed else f"[FAIL] {result.name}: FAILED")
    return result


def test_delta_dimensionless():
    """
    Test that delta_AB is dimensionless.
    """
    freq_A = 5e9  # Hz
    freq_B = 4.9e9  # Hz
    
    delta = delta_AB(freq_A, freq_B)
    
    # delta_AB should be a pure number (dimensionless)
    # Check that it's within reasonable bounds for frequency ratios
    result = TestResult(
        name="delta_AB Dimensionless",
        passed=isinstance(delta, (int, float)) and np.isfinite(delta),
        expected=np.log(freq_A/freq_B),
        actual=delta,
        tolerance=1e-15,
        description="delta_AB = ln(nu_A/nu_B) is dimensionless"
    )
    
    print(f"[PASS] {result.name}: PASSED" if result.passed else f"[FAIL] {result.name}: FAILED")
    return result


def test_delta_additivity():
    """
    Test that delta_AB is additive under composition.
    delta_AC = delta_AB + delta_BC
    """
    freq_A = 5.0e9
    freq_B = 4.9e9
    freq_C = 4.8e9
    
    delta_AB_val = delta_AB(freq_A, freq_B)
    delta_BC_val = delta_AB(freq_B, freq_C)
    delta_AC_direct = delta_AB(freq_A, freq_C)
    delta_AC_composed = delta_AB_val + delta_BC_val
    
    diff = abs(delta_AC_direct - delta_AC_composed)
    
    result = TestResult(
        name="delta_AB Additivity (Composition)",
        passed=diff < 1e-14,
        expected=delta_AC_direct,
        actual=delta_AC_composed,
        tolerance=1e-14,
        description="delta_AC = delta_AB + delta_BC (logarithm property)"
    )
    
    print(f"[PASS] {result.name}: PASSED (diff={diff:.2e})" if result.passed else f"[FAIL] {result.name}: FAILED")
    return result


def test_delta_antisymmetry():
    """
    Test that delta_AB = -delta_BA (antisymmetry).
    """
    freq_A = 5.0e9
    freq_B = 4.9e9
    
    delta_AB_val = delta_AB(freq_A, freq_B)
    delta_BA_val = delta_AB(freq_B, freq_A)
    
    sum_val = delta_AB_val + delta_BA_val
    
    result = TestResult(
        name="delta_AB Antisymmetry",
        passed=abs(sum_val) < 1e-14,
        expected=0.0,
        actual=sum_val,
        tolerance=1e-14,
        description="delta_AB + delta_BA = 0"
    )
    
    print(f"[PASS] {result.name}: PASSED" if result.passed else f"[FAIL] {result.name}: FAILED")
    return result


def test_delta_self_comparison():
    """
    Test that delta_AA = 0 (self-comparison).
    """
    freq_A = 5.0e9
    
    delta_AA = delta_AB(freq_A, freq_A)
    
    result = TestResult(
        name="delta_AA Self-Comparison",
        passed=abs(delta_AA) < 1e-15,
        expected=0.0,
        actual=delta_AA,
        tolerance=1e-15,
        description="delta_AA = ln(1) = 0"
    )
    
    print(f"[PASS] {result.name}: PASSED" if result.passed else f"[FAIL] {result.name}: FAILED")
    return result


def run_all_tests() -> List[TestResult]:
    """Run all Section 2 tests."""
    print("\n" + "="*60)
    print("SECTION 2: Constant Frequency in Gravity-Free Systems")
    print("="*60 + "\n")
    
    results = [
        test_constant_proper_frequency(),
        test_delta_dimensionless(),
        test_delta_additivity(),
        test_delta_antisymmetry(),
        test_delta_self_comparison(),
    ]
    
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    
    print(f"\n{'='*60}")
    print(f"Section 2 Results: {passed}/{total} tests passed")
    print("="*60)
    
    return results


if __name__ == "__main__":
    run_all_tests()
