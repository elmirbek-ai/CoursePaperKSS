import subprocess
import sys


def main() -> None:
    """Streamlit интерфейсин иштетет."""
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)


if __name__ == "__main__":
    main()
