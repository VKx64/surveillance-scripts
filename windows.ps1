# Define paths to the Python interpreter and script
$pythonPath = "D:\Tools\surveillance-scripts\venv\Scripts\python.exe"
$scriptPath = "D:\Tools\surveillance-scripts\screenshot.py"

# Start the Python script as a new background process
Start-Process -FilePath $pythonPath -ArgumentList $scriptPath -NoNewWindow -WindowStyle Hidden
