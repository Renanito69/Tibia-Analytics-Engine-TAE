import subprocess
import sys
import os

def instalar_dependencias():
    if os.path.exists("requirements.txt"):
        print("Verificando dependências...")
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt"
        ])

try:
    instalar_dependencias()
except Exception as erro:
    print(f"Erro ao instalar dependências: {erro}")