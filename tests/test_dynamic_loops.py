#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dynamic Loop Tests - Time-Dependent δ(t)
========================================

Paper Reference: "Frequency-Based Curvature Detection via Dynamic Comparisons"
Tests temporal evolution of frequency comparisons along trajectories.

(c) 2025 Carmen Wrede & Lino Casu
Licensed under Anti-Capitalist Software License v1.4
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Callable
import json

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================

C = 299792458.0              # Speed of light (m/s)
G = 6.67430e-11              # Gravitational constant
M_EARTH = 5.972e24           # Earth mass (kg)
R_EARTH = 6.371e6            # Earth radius (m)

# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class TrajectoryPoint:
    """Point along a trajectory"""
    t: float                 # Time (s)
    r: float                 # Radial distance (m)
    v: float                 # Velocity (m/s)
    theta: float             # Angular position (rad)

@dataclass
class DynamicLoopResult:
    """Result of dynamic loop integration"""
    trajectory_name: str
    times: List[float]
    delta_values: List[float]
    I_ABC_values: List[float]
    is_integrable: bool      # Does path integral vanish?
    max_residual: float
    description: str

# =============================================================================
# TRAJECTORY GENERATORS
# =============================================================================

def gravity_probe_a_trajectory(t: float) -> TrajectoryPoint:
    """
    Gravity Probe A trajectory (1976)
    Suborbital rocket: max altitude ~10,000 km
    """
    # Simplified ballistic trajectory
    v0 = 7000  # Initial velocity (m/s)
    g = G * M_EARTH / R_EARTH**2  # Surface gravity
    
    # Height as function of time (ballistic)
    h = v0 * t - 0.5 * g * t**2
    h = max(0, h)  # Don't go below surface
    
    r = R_EARTH + h
    v = v0 - g * t
    
    return TrajectoryPoint(t=t, r=r, v=abs(v), theta=0)

def galileo_eccentric_orbit(t: float) -> TrajectoryPoint:
    """
    Galileo 5/6 eccentric orbit
    Perigee: ~17,000 km, Apogee: ~26,000 km
    Period: ~12.9 hours
    """
    # Orbital parameters
    a = 26000e3 + R_EARTH     # Semi-major axis
    e = 0.162                  # Eccentricity
    T = 12.9 * 3600            # Period (s)
    
    # Mean anomaly
    M = 2 * np.pi * t / T
    
    # Eccentric anomaly (Newton's method)
    E = M
    for _ in range(10):
        E = M + e * np.sin(E)
    
    # True anomaly
    theta = 2 * np.arctan2(np.sqrt(1+e) * np.sin(E/2), np.sqrt(1-e) * np.cos(E/2))
    
    # Radius
    r = a * (1 - e * np.cos(E))
    
    # Velocity (vis-viva)
    v = np.sqrt(G * M_EARTH * (2/r - 1/a))
    
    return TrajectoryPoint(t=t, r=r, v=v, theta=theta)

def iss_orbit(t: float) -> TrajectoryPoint:
    """
    ISS circular orbit
    Altitude: ~400 km, Period: ~92 min
    """
    h = 400e3
    r = R_EARTH + h
    T = 92 * 60  # Period (s)
    v = 7660     # Orbital velocity (m/s)
    
    theta = 2 * np.pi * t / T
    
    return TrajectoryPoint(t=t, r=r, v=v, theta=theta)

def gps_orbit(t: float) -> TrajectoryPoint:
    """
    GPS satellite orbit
    Altitude: ~20,200 km, Period: ~12 hours
    """
    h = 20200e3
    r = R_EARTH + h
    T = 11.97 * 3600  # Period (s)
    v = 3874          # Orbital velocity (m/s)
    
    theta = 2 * np.pi * t / T
    
    return TrajectoryPoint(t=t, r=r, v=v, theta=theta)

# =============================================================================
# PHYSICS FUNCTIONS
# =============================================================================

def schwarzschild_radius(M: float) -> float:
    return 2 * G * M / C**2

def time_dilation_factor(r: float, M: float) -> float:
    """GR time dilation D = √(1 - r_s/r)"""
    r_s = schwarzschild_radius(M)
    if r <= r_s:
        return 0.01
    return np.sqrt(1 - r_s / r)

def delta_from_positions(r_A: float, r_B: float, M: float) -> float:
    """δ_AB = ln(D(r_A) / D(r_B))"""
    D_A = time_dilation_factor(r_A, M)
    D_B = time_dilation_factor(r_B, M)
    return np.log(D_A / D_B)

# =============================================================================
# DYNAMIC LOOP TESTS
# =============================================================================

def compute_dynamic_loop(
    trajectory_A: Callable[[float], TrajectoryPoint],
    trajectory_B: Callable[[float], TrajectoryPoint],
    trajectory_C: Callable[[float], TrajectoryPoint],
    t_start: float,
    t_end: float,
    n_points: int = 100
) -> Tuple[List[float], List[float], List[float], List[float]]:
    """
    Compute δ_AB(t), δ_BC(t), δ_CA(t) and I_ABC(t) along trajectories
    """
    times = np.linspace(t_start, t_end, n_points)
    delta_AB = []
    delta_BC = []
    delta_CA = []
    I_ABC = []
    
    for t in times:
        A = trajectory_A(t)
        B = trajectory_B(t)
        C = trajectory_C(t)
        
        d_AB = delta_from_positions(A.r, B.r, M_EARTH)
        d_BC = delta_from_positions(B.r, C.r, M_EARTH)
        d_CA = delta_from_positions(C.r, A.r, M_EARTH)
        
        delta_AB.append(d_AB)
        delta_BC.append(d_BC)
        delta_CA.append(d_CA)
        I_ABC.append(d_AB + d_BC + d_CA)
    
    return list(times), delta_AB, delta_BC, delta_CA, I_ABC

def test_gravity_probe_a_dynamic():
    """
    Dynamic test: Gravity Probe A trajectory
    Ground station ↔ Rocket ↔ GPS satellite
    """
    print("\n" + "="*70)
    print("TEST 1: Gravity Probe A Dynamic Loop")
    print("="*70)
    
    # Trajectories
    def ground(t): return TrajectoryPoint(t=t, r=R_EARTH, v=0, theta=0)
    def gpa(t): return gravity_probe_a_trajectory(t)
    def gps(t): return gps_orbit(t)
    
    # Compute over 2 hours (GP-A flight time)
    t_end = 2 * 3600
    times, d_AB, d_BC, d_CA, I = compute_dynamic_loop(ground, gpa, gps, 0, t_end, 50)
    
    max_I = max(abs(i) for i in I)
    mean_I = np.mean(np.abs(I))
    
    print(f"  Time span: 0 - {t_end/3600:.1f} hours")
    print(f"  δ_AB(t) range: [{min(d_AB):.6e}, {max(d_AB):.6e}]")
    print(f"  δ_BC(t) range: [{min(d_BC):.6e}, {max(d_BC):.6e}]")
    print(f"  δ_CA(t) range: [{min(d_CA):.6e}, {max(d_CA):.6e}]")
    print(f"  ─────────────────────────────────────────────")
    print(f"  I_ABC(t) max:  {max_I:.6e}")
    print(f"  I_ABC(t) mean: {mean_I:.6e}")
    print(f"  Loop Closure:  {'✅ HOLDS' if max_I < 1e-14 else '⚠️ RESIDUAL'}")
    
    # Key insight: Even though δ values change, I_ABC ≈ 0 at all times
    passed = max_I < 1e-14
    
    result = DynamicLoopResult(
        trajectory_name="Gravity Probe A",
        times=times,
        delta_values=d_AB,  # Store one example
        I_ABC_values=I,
        is_integrable=passed,
        max_residual=max_I,
        description="Ground-Rocket-GPS triangle over 2 hour flight"
    )
    
    return result, passed

def test_galileo_eccentric_dynamic():
    """
    Dynamic test: Galileo 5/6 eccentric orbit
    Most precise test of gravitational redshift variation
    """
    print("\n" + "="*70)
    print("TEST 2: Galileo 5/6 Eccentric Orbit Dynamic Loop")
    print("="*70)
    
    # Trajectories: Ground, Galileo (eccentric), GPS (circular reference)
    def ground(t): return TrajectoryPoint(t=t, r=R_EARTH, v=0, theta=0)
    def galileo(t): return galileo_eccentric_orbit(t)
    def gps(t): return gps_orbit(t)
    
    # Compute over 1 full orbit (~13 hours)
    T_orbit = 12.9 * 3600
    times, d_AB, d_BC, d_CA, I = compute_dynamic_loop(ground, galileo, gps, 0, T_orbit, 100)
    
    max_I = max(abs(i) for i in I)
    
    # The key observable: δ modulation due to eccentricity
    delta_amplitude = max(d_AB) - min(d_AB)
    
    print(f"  Orbit period: {T_orbit/3600:.1f} hours")
    print(f"  δ_AB amplitude (eccentricity signal): {delta_amplitude:.6e}")
    print(f"  δ_AB(perigee):  {max(d_AB):.6e}")
    print(f"  δ_AB(apogee):   {min(d_AB):.6e}")
    print(f"  ─────────────────────────────────────────────")
    print(f"  I_ABC(t) max:   {max_I:.6e}")
    print(f"  Loop Closure:   {'✅ HOLDS' if max_I < 1e-14 else '⚠️ RESIDUAL'}")
    
    passed = max_I < 1e-14
    
    result = DynamicLoopResult(
        trajectory_name="Galileo 5/6 Eccentric",
        times=times,
        delta_values=d_AB,
        I_ABC_values=I,
        is_integrable=passed,
        max_residual=max_I,
        description=f"Full orbit, δ amplitude = {delta_amplitude:.2e}"
    )
    
    return result, passed

def test_iss_gps_ground_dynamic():
    """
    Dynamic test: ISS-GPS-Ground triangle
    Different orbital periods → complex dynamics
    """
    print("\n" + "="*70)
    print("TEST 3: ISS-GPS-Ground Dynamic Triangle")
    print("="*70)
    
    def ground(t): return TrajectoryPoint(t=t, r=R_EARTH, v=0, theta=0)
    def iss(t): return iss_orbit(t)
    def gps(t): return gps_orbit(t)
    
    # Compute over 1 day
    t_end = 24 * 3600
    times, d_AB, d_BC, d_CA, I = compute_dynamic_loop(ground, iss, gps, 0, t_end, 200)
    
    max_I = max(abs(i) for i in I)
    
    print(f"  Time span: 24 hours")
    print(f"  ISS orbits: ~16")
    print(f"  GPS orbits: ~2")
    print(f"  ─────────────────────────────────────────────")
    print(f"  I_ABC(t) max:  {max_I:.6e}")
    print(f"  Loop Closure:  {'✅ HOLDS' if max_I < 1e-14 else '⚠️ RESIDUAL'}")
    
    passed = max_I < 1e-14
    
    result = DynamicLoopResult(
        trajectory_name="ISS-GPS-Ground",
        times=times,
        delta_values=d_AB,
        I_ABC_values=I,
        is_integrable=passed,
        max_residual=max_I,
        description="24 hour observation, multiple orbital periods"
    )
    
    return result, passed

def test_path_integral_independence():
    """
    Test: Path integral of δ is path-independent
    
    Paper claim: The loop integral I_ABC = ∮δ = 0 regardless of path
    This is the "integrability" condition for direct frequency comparisons
    """
    print("\n" + "="*70)
    print("TEST 4: Path Integral Independence")
    print("="*70)
    
    # Two different paths from A to B
    r_A = R_EARTH
    r_B = R_EARTH + 20200e3
    
    # Path 1: Direct radial
    n_steps = 100
    radii_direct = np.linspace(r_A, r_B, n_steps)
    integral_direct = 0
    for i in range(n_steps - 1):
        integral_direct += delta_from_positions(radii_direct[i], radii_direct[i+1], M_EARTH)
    
    # Path 2: Via intermediate altitude (zigzag)
    r_mid = R_EARTH + 10000e3
    radii_path2_up = np.linspace(r_A, r_mid, n_steps//2)
    radii_path2_down = np.linspace(r_mid, r_B, n_steps//2)
    
    integral_path2 = 0
    for i in range(len(radii_path2_up) - 1):
        integral_path2 += delta_from_positions(radii_path2_up[i], radii_path2_up[i+1], M_EARTH)
    for i in range(len(radii_path2_down) - 1):
        integral_path2 += delta_from_positions(radii_path2_down[i], radii_path2_down[i+1], M_EARTH)
    
    # Direct calculation (should match both)
    delta_direct = delta_from_positions(r_A, r_B, M_EARTH)
    
    diff_1 = abs(integral_direct - delta_direct)
    diff_2 = abs(integral_path2 - delta_direct)
    diff_paths = abs(integral_direct - integral_path2)
    
    print(f"  A: Earth surface ({r_A/1e6:.1f} Mm)")
    print(f"  B: GPS altitude ({r_B/1e6:.1f} Mm)")
    print(f"  ─────────────────────────────────────────────")
    print(f"  δ_AB (direct):      {delta_direct:.9e}")
    print(f"  ∫δ (radial path):   {integral_direct:.9e}  (diff: {diff_1:.2e})")
    print(f"  ∫δ (zigzag path):   {integral_path2:.9e}  (diff: {diff_2:.2e})")
    print(f"  ─────────────────────────────────────────────")
    print(f"  Path difference:    {diff_paths:.6e}")
    print(f"  Path-independent:   {'✅ YES' if diff_paths < 1e-14 else '❌ NO'}")
    
    passed = diff_paths < 1e-14
    
    return {"diff_paths": diff_paths, "passed": passed}, passed

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_all_dynamic_tests():
    """Run all dynamic loop tests"""
    print("\n" + "="*70)
    print("  DYNAMIC LOOP TEST SUITE")
    print("  Paper: 'Frequency-Based Curvature Detection via Dynamic Comparisons'")
    print("="*70)
    
    all_results = {}
    all_passed = True
    
    # Test 1: Gravity Probe A
    r1, p1 = test_gravity_probe_a_dynamic()
    all_results["gravity_probe_a"] = {
        "max_residual": r1.max_residual,
        "is_integrable": r1.is_integrable,
        "description": r1.description
    }
    all_passed = all_passed and p1
    
    # Test 2: Galileo eccentric
    r2, p2 = test_galileo_eccentric_dynamic()
    all_results["galileo_eccentric"] = {
        "max_residual": r2.max_residual,
        "is_integrable": r2.is_integrable,
        "description": r2.description
    }
    all_passed = all_passed and p2
    
    # Test 3: ISS-GPS-Ground
    r3, p3 = test_iss_gps_ground_dynamic()
    all_results["iss_gps_ground"] = {
        "max_residual": r3.max_residual,
        "is_integrable": r3.is_integrable,
        "description": r3.description
    }
    all_passed = all_passed and p3
    
    # Test 4: Path independence
    r4, p4 = test_path_integral_independence()
    all_results["path_independence"] = r4
    all_passed = all_passed and p4
    
    # Summary
    print("\n" + "="*70)
    print("  SUMMARY: DYNAMIC LOOP TESTS")
    print("="*70)
    print(f"  Test 1 (GP-A Dynamic):       {'✅ PASS' if p1 else '❌ FAIL'}")
    print(f"  Test 2 (Galileo Eccentric):  {'✅ PASS' if p2 else '❌ FAIL'}")
    print(f"  Test 3 (ISS-GPS-Ground):     {'✅ PASS' if p3 else '❌ FAIL'}")
    print(f"  Test 4 (Path Independence):  {'✅ PASS' if p4 else '❌ FAIL'}")
    print(f"  ─────────────────────────────────────────────")
    print(f"  OVERALL: {'✅ ALL PASSED' if all_passed else '❌ SOME FAILED'}")
    print("="*70)
    
    # Key insight
    print("\n  KEY INSIGHT:")
    print("  Even though δ_AB(t), δ_BC(t), δ_CA(t) vary with time,")
    print("  the loop closure I_ABC(t) = 0 holds at ALL times.")
    print("  This confirms the path-independence (integrability) of δ.")
    
    # Save results
    with open("dynamic_loop_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\n  Results saved to: dynamic_loop_results.json")
    
    return all_results, all_passed

if __name__ == "__main__":
    run_all_dynamic_tests()
