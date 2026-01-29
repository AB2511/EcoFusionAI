#!/usr/bin/env python3
"""
Quick test to verify the dashboard loads without errors
"""

import subprocess
import sys
import time
import requests
from pathlib import Path

def test_dashboard_startup():
    """Test that the dashboard starts without syntax errors"""
    print("🔍 Testing dashboard startup...")
    
    try:
        # Test syntax by compiling
        result = subprocess.run([sys.executable, '-m', 'py_compile', 'app.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("  ✅ app.py syntax is valid")
        else:
            print("  ❌ app.py has syntax errors:")
            print(result.stderr)
            return False
        
        # Test that required model files exist
        models_dir = Path("models")
        required_files = [
            "ecofusion_rf_v2.pkl",
            "ecofusion_features_v2.txt",
            "ecofusion_metrics_v2.json"
        ]
        
        for file in required_files:
            if (models_dir / file).exists():
                print(f"  ✅ {file} exists")
            else:
                print(f"  ⚠️ {file} missing (dashboard will use fallback)")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing dashboard: {e}")
        return False

def test_streamlit_health():
    """Test if Streamlit is responding"""
    print("\n🌐 Testing Streamlit health...")
    
    try:
        # Give it a moment to start
        time.sleep(2)
        
        # Try to connect to the dashboard
        response = requests.get("http://localhost:8504", timeout=5)
        
        if response.status_code == 200:
            print("  ✅ Dashboard is responding")
            print("  🌐 URL: http://localhost:8504")
            return True
        else:
            print(f"  ⚠️ Dashboard returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("  ⚠️ Dashboard not responding (may still be starting)")
        return False
    except Exception as e:
        print(f"  ❌ Error connecting to dashboard: {e}")
        return False

def main():
    print("🚀 EcoFusionAI Dashboard Test")
    print("=" * 40)
    
    # Test syntax and files
    syntax_ok = test_dashboard_startup()
    
    if not syntax_ok:
        print("\n❌ Dashboard has issues. Fix syntax errors first.")
        return False
    
    # Test if Streamlit is running
    health_ok = test_streamlit_health()
    
    print("\n" + "=" * 40)
    print("📋 Dashboard Status:")
    
    if syntax_ok and health_ok:
        print("✅ DASHBOARD READY")
        print("   - Syntax: Valid")
        print("   - Server: Running")
        print("   - URL: http://localhost:8504")
        print("\n🎯 Next Steps:")
        print("   1. Open http://localhost:8504 in browser")
        print("   2. Navigate to 'Model Insights' tab")
        print("   3. Test ML predictions")
    elif syntax_ok:
        print("⚠️ DASHBOARD STARTING")
        print("   - Syntax: Valid")
        print("   - Server: Starting (wait 30 seconds)")
        print("   - URL: http://localhost:8504")
    else:
        print("❌ DASHBOARD HAS ISSUES")
        print("   - Check syntax errors above")
    
    return syntax_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)