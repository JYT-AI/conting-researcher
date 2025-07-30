#!/usr/bin/env python3
"""
Basic import test for conting-researcher package
"""
import pytest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_basic_imports():
    """Test that basic imports work correctly"""
    try:
        from gpt_researcher.agent import GPTResearcher
        from gpt_researcher.config.config import Config
        from gpt_researcher.actions.retriever import get_retriever
        print("✅ All basic imports successful")
        assert True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        assert False, f"Import failed: {e}"

def test_gpt_researcher_class_exists():
    """Test that GPTResearcher class exists and can be imported"""
    try:
        from gpt_researcher.agent import GPTResearcher

        # Just check that the class exists
        assert GPTResearcher is not None
        assert hasattr(GPTResearcher, '__init__')
        print("✅ GPTResearcher class exists and is importable")

    except Exception as e:
        print(f"❌ GPTResearcher class test failed: {e}")
        assert False, f"GPTResearcher class test failed: {e}"

def test_config_loading():
    """Test that Config can be loaded"""
    try:
        from gpt_researcher.config.config import Config
        
        config = Config()
        assert config is not None
        print("✅ Config loading successful")
        
    except Exception as e:
        print(f"❌ Config loading failed: {e}")
        assert False, f"Config loading failed: {e}"

if __name__ == "__main__":
    print("🧪 Running basic import tests for conting-researcher...")
    test_basic_imports()
    test_gpt_researcher_class_exists()
    test_config_loading()
    print("🎉 All basic tests passed!")
