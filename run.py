import subprocess
from pathlib import Path

XMRIG_DIR = Path("C:/xmrig")
XMRIG_EXE = XMRIG_DIR / "xmrig.exe"

def run_xmrig_in_background():
    subprocess.Popen([str(XMRIG_EXE)], creationflags=subprocess.CREATE_NO_WINDOW)

def main():
    # Uruchamianie XMRig w tle
    run_xmrig_in_background()

if __name__ == "__main__":
    main()
