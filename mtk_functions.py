import subprocess
import os

def run_mtk_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error: {str(e)}"

def check_preloader():
    return run_mtk_command("mtk da seccfg unlock")

def frp_remove():
    commands = [
        "mtk da seccfg unlock",
        "mtk frp unlock"
    ]
    output = ""
    for cmd in commands:
        output += f"\n--- {cmd} ---\n"
        output += run_mtk_command(cmd)
    return output