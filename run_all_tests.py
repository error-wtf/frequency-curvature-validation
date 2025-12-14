#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Frequency-Based Curvature Detection - Master Test Runner
=========================================================

Runs all validation tests for the paper:
"Frequency-Based Curvature Detection via Dynamic Comparisons"

Authors: Carmen N. Wrede, Lino P. Casu, Bingsi

Usage:
    python run_all_tests.py
    python run_all_tests.py --verbose
    python run_all_tests.py --section 4

(c) 2025 Carmen Wrede & Lino Casu
Licensed under Anti-Capitalist Software License v1.4
"""

import subprocess
import sys
import os
import json
from datetime import datetime

def run_pytest():
    """Run all tests with pytest"""
    print("=" * 70)
    print("  FREQUENCY-BASED CURVATURE DETECTION - VALIDATION SUITE")
    print("  Paper: 'Frequency-Based Curvature Detection via Dynamic Comparisons'")
    print("=" * 70)
    print()
    
    # Change to tests directory
    tests_dir = os.path.join(os.path.dirname(__file__), "tests")
    
    # Run pytest
    result = subprocess.run(
        [sys.executable, "-m", "pytest", tests_dir, "-v", "--tb=short"],
        capture_output=False
    )
    
    return result.returncode

def run_individual_tests():
    """Run individual test modules and collect results"""
    print("=" * 70)
    print("  RUNNING INDIVIDUAL TEST MODULES")
    print("=" * 70)
    print()
    
    tests_dir = os.path.join(os.path.dirname(__file__), "tests")
    results = {}
    total_passed = 0
    total_tests = 0
    
    test_files = [
        "test_section2_constant_frequency.py",
        "test_section3_first_order_shifts.py",
        "test_section4_loop_closure.py",
        "test_section5_relation_to_gr.py",
        "test_section6_ssz_integration.py",
        "test_section7_conclusions.py",
        "test_ssz_physics.py",
        "test_nsr_ngr_separation.py",
        "test_dynamic_loops.py",
        "test_experimental_validation.py",
    ]
    
    for test_file in test_files:
        test_path = os.path.join(tests_dir, test_file)
        if os.path.exists(test_path):
            print(f"Running {test_file}...")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", test_path, "-v", "--tb=short"],
                capture_output=True,
                text=True
            )
            
            # Parse results
            passed = result.stdout.count(" PASSED")
            failed = result.stdout.count(" FAILED")
            
            results[test_file] = {
                "passed": passed,
                "failed": failed,
                "total": passed + failed
            }
            
            total_passed += passed
            total_tests += passed + failed
            
            status = "[PASS]" if failed == 0 else "[FAIL]"
            print(f"  {status} {test_file}: {passed}/{passed+failed}")
    
    # Summary
    print()
    print("=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print(f"  Total Tests:  {total_tests}")
    print(f"  Passed:       {total_passed}")
    print(f"  Failed:       {total_tests - total_passed}")
    print(f"  Pass Rate:    {total_passed/total_tests*100:.1f}%")
    print("=" * 70)
    
    # Save results
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_tests": total_tests,
        "total_passed": total_passed,
        "pass_rate": total_passed / total_tests if total_tests > 0 else 0,
        "modules": results
    }
    
    with open("test_results.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to: test_results.json")
    
    return 0 if total_passed == total_tests else 1

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--individual":
        return run_individual_tests()
    else:
        return run_pytest()

if __name__ == "__main__":
    sys.exit(main())
