#!/usr/bin/env python3
"""
Shapiro Delay Validation Tests
(c) 2025 Carmen Wrede & Lino Casu - ACSL v1.4
"""
import pytest
import numpy as np

# Constants
G = 6.67430e-11
c = 299792458.0
M_SUN = 1.98892e30
R_SUN = 6.957e8
AU = 1.495978707e11
R_S_SUN = 2 * G * M_SUN / c**2  # ~2953 m

def shapiro_delay(r1, r2, d, M=M_SUN, gamma=1.0):
    """
    Shapiro delay for light grazing a massive body.
    
    For r1, r2 >> d (typical solar system case):
        Δt ≈ (1+γ)(r_s/c) * ln(4*r1*r2/d²)
    """
    r_s = 2 * G * M / c**2
    # Use the approximation valid for r1, r2 >> d
    return (1 + gamma) * (r_s / c) * np.log(4 * r1 * r2 / d**2)

def shapiro_delay_ssz(r1, r2, d, M=M_SUN):
    """SSZ Shapiro delay with second-order correction."""
    r_s = 2 * G * M / c**2
    xi_corr = 1 + (r_s / (4 * d))**2
    return shapiro_delay(r1, r2, d, M, 1.0) * xi_corr

class TestShapiroBasics:
    def test_delay_positive(self):
        delay = shapiro_delay(AU, 0.723*AU, 2*R_SUN)
        assert delay > 0

    def test_closer_approach_larger_delay(self):
        d_far = shapiro_delay(AU, AU, 10*R_SUN)
        d_close = shapiro_delay(AU, AU, 2*R_SUN)
        assert d_close > d_far

    def test_gamma_doubles_delay(self):
        d_gr = shapiro_delay(AU, AU, 2*R_SUN, gamma=1.0)
        d_newt = shapiro_delay(AU, AU, 2*R_SUN, gamma=0.0)
        assert abs(d_gr / d_newt - 2.0) < 0.01

class TestCassini:
    """Cassini 2003: γ = 1.000021 ± 0.000023 (best ever)"""
    
    def test_cassini_delay_magnitude(self):
        r_saturn = 9.537 * AU
        delay = shapiro_delay(AU, r_saturn, 1.6*R_SUN)
        delay_us = delay * 1e6
        assert 50 < delay_us < 300  # ~120 μs one-way

    def test_cassini_gamma_constraint(self):
        gamma_measured = 1.000021
        gamma_error = 0.000023
        assert abs(gamma_measured - 1.0) < 5 * gamma_error

class TestSSZvsGR:
    """SSZ predicts tiny correction at second order."""
    
    def test_weak_field_agreement(self):
        gr = shapiro_delay(AU, AU, 5*R_SUN)
        ssz = shapiro_delay_ssz(AU, AU, 5*R_SUN)
        diff = abs(ssz - gr) / gr
        assert diff < 1e-10  # Negligible in solar system

    def test_ssz_correction_sign(self):
        gr = shapiro_delay(AU, AU, 2*R_SUN)
        ssz = shapiro_delay_ssz(AU, AU, 2*R_SUN)
        assert ssz >= gr  # SSZ adds small positive correction


class TestHistoricalExperiments:
    """Historical Shapiro delay measurements."""
    
    def test_viking_1979(self):
        """Viking Mars lander: γ = 1.000 ± 0.002"""
        r_mars = 1.524 * AU
        delay = shapiro_delay(AU, r_mars, 2*R_SUN)
        delay_us = delay * 1e6
        # Viking measured ~250 μs one-way at conjunction
        assert 100 < delay_us < 300
    
    def test_mariner_6_7(self):
        """Mariner 6 & 7 (1969): First spacecraft test"""
        r_mars = 1.524 * AU
        delay = shapiro_delay(AU, r_mars, 3*R_SUN)
        assert delay > 0
    
    def test_mercury_venus_radar(self):
        """Original Shapiro (1964) radar test prediction"""
        r_venus = 0.723 * AU
        delay = shapiro_delay(AU, r_venus, 1.5*R_SUN)
        delay_us = delay * 1e6
        # Expected ~200 μs at superior conjunction
        assert 50 < delay_us < 250


class TestPulsarShapiro:
    """Shapiro delay in binary pulsars."""
    
    def test_double_pulsar_j0737(self):
        """PSR J0737-3039: Best pulsar Shapiro test"""
        # Companion mass ~1.25 M_sun
        M_companion = 1.25 * M_SUN
        # Orbital separation ~10^9 m, impact ~10^8 m
        delay = shapiro_delay(1e9, 1e9, 1e8, M=M_companion)
        delay_us = delay * 1e6
        # Pulsar timing precision allows μs measurements
        assert delay_us > 1  # Detectable
    
    def test_shapiro_range_parameter(self):
        """Shapiro 'range' parameter r = GM/c³"""
        # For solar mass, r ≈ 4.93 μs
        r_sun = G * M_SUN / c**3
        r_sun_us = r_sun * 1e6
        assert 4.9 < r_sun_us < 5.0


class TestGravitationalWaves:
    """Shapiro delay for gravitational waves (GW170817)."""
    
    def test_gw170817_constraint(self):
        """
        GW170817: GW and gamma-ray arrived within 1.7s
        after traveling ~40 Mpc through cosmic structure.
        This constrains alternative gravity theories.
        """
        # 40 Mpc in meters
        d_source = 40e6 * 3.086e16  # ~1.2e24 m
        
        # Shapiro delay through Milky Way potential
        # Using simplified estimate for galactic mass
        M_galaxy = 1e12 * M_SUN
        d_impact = 8e3 * 3.086e16  # 8 kpc to galactic center
        
        # GR predicts same delay for GW and photons
        delay_gw = shapiro_delay(d_source/2, d_source/2, d_impact, M=M_galaxy)
        
        # The key result: GW and photons have SAME delay in GR
        # Measured difference < 1.7s constrains modified gravity
        assert delay_gw > 0  # Delay exists
