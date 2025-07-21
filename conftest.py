"""
Pytest configuration file for leetcode problems test suite.
"""
import pytest

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "graph: marks tests related to graph algorithms")
    config.addinivalue_line("markers", "dynamic_programming: marks tests related to DP problems")