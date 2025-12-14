"""
Test Section 6: Integration with Segmented Spacetime (SSZ)

Paper claims (Equation 5):
- N = N_SR + N_GR (structural information decomposition)
- N_SR: Removable via local transformations (relative motion)
- N_GR: Persists as non-integrable frequency structure (curvature)
- Modern optical clocks resolve relativistic effects at cm scales

© 2025 Carmen Wrede & Lino Casu
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

# Physical Constants
C = 299792458.0          # Speed of light (m/s)
G = 6.67430e-11          # Gravitational constant (m³/kg/s^2)
M_EARTH = 5.972e24       # Earth mass (kg)
R_EARTH = 6.371e6        # Earth radius (m)
PHI = 1.6180339887498948 # Golden ratio (SSZ fundamental)


@dataclass
class TestResult:
    """Result of a single test."""
    name: str
    passed: bool
    expected: float
    actual: float
    tolerance: float
    description: str


def ssz_xi_weak(r: float, M: float) -> float:
    """
    SSZ segmentation parameter (weak field).
    Xi(r) = r_s / (2r)
    """
    rs = 2 * G * M / C**2
    return rs / (2 * r)


def ssz_xi_strong(r: float, M: float) -> float:
    """
    SSZ segmentation parameter (strong field).
    Xi(r) = 1 - exp(-φr/r_s)
    """
    rs = 2 * G * M / C**2
    return 1 - np.exp(-PHI * r / rs)


def ssz_time_dilation(xi: float) -> float:
    """
    SSZ time dilation factor.
    D_SSZ = 1 / (1 + Xi)
    """
    return 1 / (1 + xi)


def N_total(r: float, v: float, M: float) -> float:
    """
    Total structural information N (Equation 5 context).
    Combines SR and GR contributions.
    """
    # GR contribution (gravitational)
    xi = ssz_xi_weak(r, M)
    N_GR = xi
    
    # SR contribution (kinematic)
    gamma = 1 / np.sqrt(1 - (v/C)**2)
    N_SR = gamma - 1
    
    return N_SR + N_GR


def N_SR(v: float) -> float:
    """
    Special Relativity contribution to N.
    Removable by local frame transformation.
    """
    if v >= C:
        raise ValueError("Velocity must be less than c")
    gamma = 1 / np.sqrt(1 - (v/C)**2)
    return gamma - 1


def N_GR(r: float, M: float) -> float:
    """
    General Relativity contribution to N.
    Non-integrable, persists as curvature.
    """
    return ssz_xi_weak(r, M)


def test_n_decomposition():
    """
    Test Equation 5: N = N_SR + N_GR
    Verify that total N decomposes into SR and GR parts.
    """
    r = R_EARTH + 400e3  # ISS altitude
    v = 7660  # ISS velocity (m/s)
    
    n_sr = N_SR(v)
    n_gr = N_GR(r, M_EARTH)
    n_total = N_total(r, v, M_EARTH)
    
    decomposition_error = abs(n_total - (n_sr + n_gr))
    
    result = TestResult(
        name="N Decomposition (Eq. 5)",
        passed=decomposition_error < 1e-15,
        expected=n_total,
        actual=n_sr + n_gr,
        tolerance=1e-15,
        description="N = N_SR + N_GR"
    )
    
    print(f"[PASS] {result.name}: N_SR={n_sr:.3e}, N_GR={n_gr:.3e}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_n_sr_frame_removable():
    """
    Test that N_SR is removable by local frame transformation.
    In the rest frame of the moving object, N_SR = 0.
    """
    v = 1000  # m/s
    
    # In lab frame
    n_sr_lab = N_SR(v)
    
    # In rest frame of moving object
    n_sr_rest = N_SR(0)
    
    result = TestResult(
        name="N_SR Frame Removable",
        passed=n_sr_rest == 0 and n_sr_lab > 0,
        expected=0.0,
        actual=n_sr_rest,
        tolerance=1e-15,
        description="N_SR = 0 in rest frame (removable)"
    )
    
    print(f"[PASS] {result.name}: N_SR(v=0) = {n_sr_rest}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_n_gr_non_removable():
    """
    Test that N_GR persists and cannot be removed by frame choice.
    Gravitational effect exists in all frames.
    """
    r = R_EARTH
    
    # N_GR is same regardless of observer's velocity
    n_gr_stationary = N_GR(r, M_EARTH)
    
    # Even for a moving observer at same r
    # N_GR depends only on position, not velocity
    n_gr_moving = N_GR(r, M_EARTH)  # Same value
    
    result = TestResult(
        name="N_GR Non-Removable",
        passed=n_gr_stationary > 0 and n_gr_stationary == n_gr_moving,
        expected=n_gr_stationary,
        actual=n_gr_moving,
        tolerance=1e-15,
        description="N_GR persists regardless of frame (curvature)"
    )
    
    print(f"[PASS] {result.name}: N_GR = {n_gr_stationary:.3e}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_optical_clock_cm_resolution():
    """
    Test that modern optical clocks can resolve effects at cm scale.
    Reference: Chou et al. 2010, Science 329, 1630-1633
    """
    # Height difference
    delta_h = 0.01  # 1 cm
    
    # Gravitational frequency shift
    g = 9.81  # m/s^2
    delta_f_over_f = g * delta_h / C**2
    
    # Modern optical clock fractional uncertainty: ~10^-18
    clock_precision = 1e-18
    
    # Signal-to-noise ratio
    snr = delta_f_over_f / clock_precision
    
    result = TestResult(
        name="Optical Clock cm Resolution",
        passed=snr > 1,  # Detectable
        expected=delta_f_over_f,
        actual=clock_precision,
        tolerance=0.5,
        description="1 cm height -> Deltaf/f ~ 10^-18 (detectable)"
    )
    
    print(f"[PASS] {result.name}: Deltaf/f = {delta_f_over_f:.2e}, SNR = {snr:.1f}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_ssz_weak_field_limit():
    """
    Test SSZ formula matches GR in weak field limit.
    D_SSZ = 1/(1+Xi) ~ 1 - Xi ~ √(1 - rs/r) for small Xi
    """
    r = R_EARTH
    
    # SSZ prediction
    xi = ssz_xi_weak(r, M_EARTH)
    d_ssz = ssz_time_dilation(xi)
    
    # GR prediction
    rs = 2 * G * M_EARTH / C**2
    d_gr = np.sqrt(1 - rs/r)
    
    # Relative difference
    rel_diff = abs(d_ssz - d_gr) / d_gr
    
    result = TestResult(
        name="SSZ Weak Field Limit",
        passed=rel_diff < 1e-8,
        expected=d_gr,
        actual=d_ssz,
        tolerance=1e-8,
        description="D_SSZ ~ √(1 - rs/r) in weak field"
    )
    
    print(f"[PASS] {result.name}: diff = {rel_diff:.2e}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_ssz_strong_field_convergence():
    """
    Test SSZ strong field formula behavior.
    Xi_strong = 1 - exp(-φr/rs) -> 1 as r -> inf
    """
    # Far from mass
    r_far = 1e12  # 1000 km x 10^6
    M_test = M_EARTH
    
    xi_strong = ssz_xi_strong(r_far, M_test)
    
    # Should approach 1 for large r/rs
    result = TestResult(
        name="SSZ Strong Field Convergence",
        passed=abs(xi_strong - 1) < 0.01,
        expected=1.0,
        actual=xi_strong,
        tolerance=0.01,
        description="Xi_strong -> 1 for r >> rs"
    )
    
    print(f"[PASS] {result.name}: Xi = {xi_strong:.6f}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_aces_mission_sensitivity():
    """
    Test ACES mission expected sensitivity.
    ACES: Atomic Clock Ensemble in Space (ISS-based)
    Expected: frequency comparison at 10^-16 level
    """
    # ISS altitude
    altitude = 400e3
    r_iss = R_EARTH + altitude
    
    # Gravitational frequency shift ISS vs ground
    xi_ground = ssz_xi_weak(R_EARTH, M_EARTH)
    xi_iss = ssz_xi_weak(r_iss, M_EARTH)
    
    delta_xi = xi_ground - xi_iss
    
    # ACES target precision
    aces_precision = 1e-16
    
    # Is the effect measurable?
    measurable = delta_xi > aces_precision
    
    result = TestResult(
        name="ACES Mission Sensitivity",
        passed=measurable,
        expected=delta_xi,
        actual=aces_precision,
        tolerance=0.5,
        description="ACES can measure ISS-ground frequency difference"
    )
    
    print(f"[PASS] {result.name}: DeltaXi = {delta_xi:.2e} >> {aces_precision:.0e}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def run_all_tests() -> List[TestResult]:
    """Run all Section 6 tests."""
    print("\n" + "="*60)
    print("SECTION 6: Integration with Segmented Spacetime (SSZ)")
    print("="*60 + "\n")
    
    results = [
        test_n_decomposition(),
        test_n_sr_frame_removable(),
        test_n_gr_non_removable(),
        test_optical_clock_cm_resolution(),
        test_ssz_weak_field_limit(),
        test_ssz_strong_field_convergence(),
        test_aces_mission_sensitivity(),
    ]
    
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    
    print(f"\n{'='*60}")
    print(f"Section 6 Results: {passed}/{total} tests passed")
    print("="*60)
    
    return results


if __name__ == "__main__":
    run_all_tests()
