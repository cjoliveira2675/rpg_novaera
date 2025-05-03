import os
import sys
import subprocess

# Define a raiz do projeto como PYTHONPATH
project_root = os.path.dirname(os.path.abspath(__file__))
os.environ["PYTHONPATH"] = project_root

# Executa o módulo principal com o Flet
subprocess.run([sys.executable, "-m", "app.main"])
