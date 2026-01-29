#!/usr/bin/env python3
"""
EcoFusionAI ML Pipeline Runner
Executes the notebook to generate ML artifacts for the dashboard
"""

import subprocess
import sys
from pathlib import Path

def run_notebook():
    """Execute the ML notebook to generate artifacts"""
    notebook_path = Path("notebooks/EcofusionAI_v2.ipynb")
    
    if not notebook_path.exists():
        print(f"❌ Notebook not found: {notebook_path}")
        return False
    
    try:
        print("🚀 Running ML pipeline notebook...")
        print("This will generate:")
        print("  - models/ecofusion_rf_v2.pkl")
        print("  - models/ecofusion_features_v2.txt") 
        print("  - models/ecofusion_metrics_v2.json")
        print("  - data/ecofusion_ml_ready.csv")
        print()
        
        # Execute notebook using nbconvert
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            str(notebook_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ ML pipeline completed successfully!")
            print("You can now run the dashboard with: streamlit run app.py")
            return True
        else:
            print("❌ Notebook execution failed:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ Jupyter not found. Install with: pip install jupyter")
        return False
    except Exception as e:
        print(f"❌ Error running notebook: {e}")
        return False

if __name__ == "__main__":
    success = run_notebook()
    sys.exit(0 if success else 1)