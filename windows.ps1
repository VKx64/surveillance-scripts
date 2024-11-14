# PowerShell script to activate a virtual environment and run a Python script

# Set paths
$venvPath = "D:\Tools\surveillance-scripts\venv"  # Path to your virtual environment folder
$scriptPath = "D:\Tools\surveillance-scripts\screenshot.py"  # Path to the Python script you want to run

# Activate the virtual environment
& "$venvPath\Scripts\Activate.ps1"

# Run the Python script
python $scriptPath
