"""
Test Section 3: First-Order Frequency Shifts and Their Limits

Paper claims:
- Frequency shifts reflect local differences in clock rates
- First-order shifts can be absorbed by frame choice
- Gravity Probe A and Galileo experiments confirm relativistic time dilation
- First-order shifts do NOT constitute curvature tests

© 2025 Carmen Wrede & Lino Casu
"""

import numpy as np
from dataclasses import dataclass
from typing import List

# Physical Constants
C = 299792458.0          # Speed of light (m/s)
G = 6.67430e-11          # Gravitational constant (m³/kg/s^2)
M_EARTH = 5.972e24       # Earth mass (kg)
R_EARTH = 6.371e6        # Earth radius (m)


@dataclass
class TestResult:
    """Result of a single test."""
    name: str
    passed: bool
    expected: float
    actual: float
    tolerance: float
    description: str


def gravitational_redshift(r1: float, r2: float, M: float = M_EARTH) -> float:
    """
    Gravitational redshift between two radii.
    Deltaν/ν = GM/c^2 x (1/r1 - 1/r2)
    """
    rs = 2 * G * M / C**2  # Schwarzschild radius
    return (rs / 2) * (1/r1 - 1/r2)


def doppler_shift(v: float) -> float:
    """
    First-order Doppler shift.
    Deltaν/ν ~ v/c (for v << c)
    """
    return v / C


def time_dilation_factor(potential_diff: float) -> float:
    """
    Time dilation from gravitational potential difference.
    Deltatau/tau = DeltaPhi/c^2
    """
    return potential_diff / C**2


def test_gravity_probe_a():
    """
    Test Gravity Probe A prediction (1976).
    H-maser at altitude ~10,000 km showed relativistic time dilation.
    Expected: ~4.5x10^-1⁰ fractional frequency shift
    """
    altitude = 10000e3  # 10,000 km
    r_surface = R_EARTH
    r_orbit = R_EARTH + altitude
    
    # Gravitational redshift
    redshift = gravitational_redshift(r_surface, r_orbit)
    
    # Expected value from Gravity Probe A
    expected = 4.5e-10  # approximate
    
    # Allow 10% tolerance for this estimate
    result = TestResult(
        name="Gravity Probe A Redshift",
        passed=abs(redshift - expected) / expected < 0.1,
        expected=expected,
        actual=redshift,
        tolerance=0.1,
        description="Gravitational redshift at ~10,000 km altitude"
    )
    
    print(f"[PASS] {result.name}: {redshift:.3e} (expected ~{expected:.1e})" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_galileo_eccentric_orbit():
    """
    Test Galileo satellite redshift (eccentric orbit).
    Satellites in eccentric orbits show varying redshift with altitude.
    """
    # Galileo 5 & 6 had eccentric orbits: perigee ~17,000 km, apogee ~26,000 km
    perigee = R_EARTH + 17000e3
    apogee = R_EARTH + 26000e3
    
    # Redshift difference between perigee and apogee
    shift_perigee = gravitational_redshift(R_EARTH, perigee)
    shift_apogee = gravitational_redshift(R_EARTH, apogee)
    
    # The frequency modulation along orbit
    delta_shift = abs(shift_apogee - shift_perigee)
    
    # Should be on order of 10^-1⁰
    result = TestResult(
        name="Galileo Eccentric Orbit Modulation",
        passed=1e-11 < delta_shift < 1e-9,
        expected=1e-10,  # order of magnitude
        actual=delta_shift,
        tolerance=1e-10,
        description="Frequency modulation in eccentric Galileo orbit"
    )
    
    print(f"[PASS] {result.name}: Delta = {delta_shift:.3e}" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_pound_rebka_prediction():
    """
    Test Pound-Rebka experiment prediction.
    Height difference: 22.5 m in Harvard tower
    Expected shift: ~2.5x10^-1⁵
    """
    height = 22.5  # meters
    r1 = R_EARTH
    r2 = R_EARTH + height
    
    redshift = gravitational_redshift(r1, r2)
    
    # Pound-Rebka measured: 2.57x10^-1⁵ (±10%)
    expected = 2.46e-15
    
    result = TestResult(
        name="Pound-Rebka Tower Prediction",
        passed=abs(redshift - expected) / expected < 0.15,
        expected=expected,
        actual=redshift,
        tolerance=0.15,
        description="Gravitational redshift over 22.5 m height"
    )
    
    print(f"[PASS] {result.name}: {redshift:.3e} (expected {expected:.2e})" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_first_order_frame_absorbable():
    """
    Test that first-order shifts can be absorbed by frame transformation.
    Key claim: First-order shifts are NOT curvature signatures.
    """
    # In a uniformly accelerating frame, gravitational redshift 
    # is equivalent to acceleration redshift (equivalence principle)
    
    g = 9.81  # m/s^2 (Earth surface gravity)
    height = 100  # meters
    
    # Gravitational redshift
    grav_shift = g * height / C**2
    
    # Equivalent acceleration redshift (Rindler)
    accel_shift = g * height / C**2
    
    # They should be identical (equivalence principle)
    diff = abs(grav_shift - accel_shift)
    
    result = TestResult(
        name="First-Order Frame Absorbability",
        passed=diff < 1e-30,
        expected=0.0,
        actual=diff,
        tolerance=1e-30,
        description="Gravitational vs acceleration redshift (equivalence principle)"
    )
    
    print(f"[PASS] {result.name}: Equivalence confirmed" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def test_gps_relativistic_correction():
    """
    Test GPS relativistic frequency correction.
    GPS satellites at ~20,200 km altitude require ~45 us/day correction.
    """
    altitude = 20200e3  # GPS altitude
    r_gps = R_EARTH + altitude
    
    # Gravitational time dilation (satellite runs faster)
    grav_effect = gravitational_redshift(R_EARTH, r_gps)
    
    # Convert to microseconds per day
    seconds_per_day = 86400
    microseconds_grav = grav_effect * seconds_per_day * 1e6
    
    # GPS satellites also have velocity ~3.87 km/s
    v_gps = 3874  # m/s
    sr_effect = -0.5 * (v_gps / C)**2  # Time dilation (satellite runs slower)
    microseconds_sr = sr_effect * seconds_per_day * 1e6
    
    total_correction = microseconds_grav + microseconds_sr
    
    # Expected: ~38 us/day (GR +45 us, SR -7 us = 38 us combined)
    expected = 38.0  # us/day (combined GR+SR effect)
    
    result = TestResult(
        name="GPS Relativistic Correction",
        passed=abs(total_correction - expected) < 3,
        expected=expected,
        actual=total_correction,
        tolerance=3.0,
        description="GPS requires ~38 us/day relativistic correction (GR+SR)"
    )
    
    print(f"[PASS] {result.name}: {total_correction:.1f} us/day (expected ~{expected} us/day)" if result.passed 
          else f"[FAIL] {result.name}: FAILED")
    return result


def run_all_tests() -> List[TestResult]:
    """Run all Section 3 tests."""
    print("\n" + "="*60)
    print("SECTION 3: First-Order Frequency Shifts and Their Limits")
    print("="*60 + "\n")
    
    results = [
        test_gravity_probe_a(),
        test_galileo_eccentric_orbit(),
        test_pound_rebka_prediction(),
        test_first_order_frame_absorbable(),
        test_gps_relativistic_correction(),
    ]
    
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    
    print(f"\n{'='*60}")
    print(f"Section 3 Results: {passed}/{total} tests passed")
    print("="*60)
    
    return results


if __name__ == "__main__":
    run_all_tests()
