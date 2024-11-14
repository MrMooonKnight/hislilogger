import os
import subprocess
import argparse
import shutil
import sys
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Configuration
GITHUB_REPO = "https://github.com/MrMooonKnight/hislilogger-application"
DOWNLOAD_DIR = "./application"
VENV_DIR = os.path.join(DOWNLOAD_DIR, "venv")


def print_banner():
    banner = pyfiglet.figlet_format("Hislilogger", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.GREEN + "Welcome to Hislilogger! A tool for managing your project with ease.\n")


def automated_installation():
    """Install everything and setup automatically"""
    print(Fore.YELLOW + "Starting Automated Installation...")
    download_project()
    install_requirements()
    start_app()


###       HELPER FUNCTIONS      ###
def run_command(command, cwd=None):
    """Run a shell command and check for errors"""
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e}")
        sys.exit(1)


###        DOWNLOAD FUNCTION      ###
def download_project():
    """Downloads the Project From Github"""
    if os.path.exists(DOWNLOAD_DIR):
        choice = input(Fore.YELLOW + "Project already exists. Do you want to download it again? (y/n): ").strip().lower()
        if choice != 'y':
            print(Fore.CYAN + "Download Skipped.")
            return
        print(Fore.YELLOW + "Removing existing project folder...")
        shutil.rmtree(DOWNLOAD_DIR)

    print(Fore.GREEN + "Downloading Project...")
    run_command(["git", "clone", GITHUB_REPO, DOWNLOAD_DIR])
    print(Fore.GREEN + "Project Downloaded Successfully")


###       INSTALL FUNCTION    ###
def install_requirements():
    """Sets up a virtual environment and installs dependencies"""
    if not os.path.exists(DOWNLOAD_DIR):
        print(Fore.RED + "Project folder not found. Please download the project first.")
        return

    print(Fore.GREEN + "Creating the virtual environment...")
    run_command(["python3", "-m", "venv", VENV_DIR])
    print(Fore.GREEN + "Virtual environment created.")

    pip_path = os.path.join(VENV_DIR, "bin", "pip")
    requirements_file = os.path.join(DOWNLOAD_DIR, "requirements.txt")

    if os.path.exists(requirements_file):
        print(Fore.GREEN + "Installing requirements...")
        run_command([pip_path, "install", "-r", requirements_file])
        print(Fore.GREEN + "Requirements installed successfully.")
    else:
        print(Fore.RED + "requirements.txt not found.")


    fastfetch_path = os.path.join(DOWNLOAD_DIR,"fastfetch")
    if not os.path.exists(fastfetch_path):
        print(Fore.RED + "fastfetch not found in the project.")
        return
    else:
    	run_command(["chmod","+x",fastfetch_path])
    	print(Fore.GREEN + "fastfetch setup completed.")


###    START FUNCTION   ###
def start_app():
    """Starts the Flask application by activating the virtual environment and running app.py"""
    if not os.path.exists(VENV_DIR):
        print(Fore.RED + "Virtual environment not found. Please run the install command first.")
        return

    activate_venv = os.path.join(VENV_DIR, "bin", "activate")
    app_file = os.path.join(DOWNLOAD_DIR, "app.py")


    fastfetch_path = os.path.join(DOWNLOAD_DIR,"fastfetch")
    if not os.path.exists(fastfetch_path):
        print(Fore.RED + "fastfetch not found in the project.")
    else:
    	run_command([fastfetch_path])


    if not os.path.exists(app_file):
        print(Fore.RED + "app.py not found in the project.")
        return

    print(Fore.GREEN + "Starting the Flask Application...")

    try:
        subprocess.run(f"source {activate_venv} && python3 {app_file}", shell=True, check=True, executable='/bin/bash')
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e}")
        sys.exit(1)
    




###    RESTART FUNCTION    ###
def restart_app():
    """Restarts the Flask application"""
    print(Fore.YELLOW + "Restarting the Flask application...")
    start_app()


###    MAIN CLI LOGIC    ###
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Manage your project with ease!")
    parser.add_argument("-a", action="store_true", help="Automated Installation")
    parser.add_argument("-d", "--download", action="store_true", help="Download the project from GitHub")
    parser.add_argument("-i", "--install", action="store_true", help="Install the application requirements")
    parser.add_argument("-s", "--start", action="store_true", help="Start the Flask application")
    parser.add_argument("-r", "--restart", action="store_true", help="Restart the Flask application")

    args = parser.parse_args()

    if args.a:
        automated_installation()
    elif args.download:
        download_project()
    elif args.install:
        install_requirements()
    elif args.start:
        start_app()
    elif args.restart:
        restart_app()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
