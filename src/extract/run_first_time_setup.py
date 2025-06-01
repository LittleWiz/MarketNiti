import subprocess
import sys
import os

def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    print(f"\nRunning {script_name} ...")
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        print(f"Error: {script_name} failed with exit code {result.returncode}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    run_script("setupsqlite.py")
    run_script("check_sqlite_setup.py")
    run_script("stock_master_data.py")
    print("\nAll setup steps completed successfully.")