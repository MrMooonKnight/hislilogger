import os
import subprocess
import argparse
import shutil
import sys


# Configuration
GITHUB_REPO = "https://github.com/MrMooonKnight/hislilogger-application"
DOWNLOAD_DIR = "./application"
VENV_DIR = os.path.join(DOWNLOAD_DIR, "venv")



def	automated_installation():
	print("adsf")



###       HELPER FUNCTIONS      ###
def run_command(command, cwd=None):

	"""Run a shell command anc check for errors if any"""

	try:
		subprocess.run(command, cwd=cwd, check=True)
	except subprocess.CalledProcessError as e:
		print(f"Error: {e}")
		sys.exit(1)



###        DOWNLOAD FUNCTION      ###
def download_project():
	
	"""Downloads the Project From Github"""

	if os.path.exists(DOWNLOAD_DIR):
		choice=input("Project already exists. Do you want to download it again? (y/n):").strip().lower()
		if choice != 'y':
			print("Download Skipped.")
			return
		print("Removing existing project folder...")
		shutil.rmtree(DOWNLOAD_DIR)

	print("Downloading Project...")
	run_command(["git", "clone", GITHUB_REPO, DOWNLOAD_DIR])
	print("Project Downloaded Successfully")



###       INSTALL FUNCTION    ###
def	install_requirements():
	
	"""Sets up a virtual environment and installs dependencies"""
	if not os.path.exists(DOWNLOAD_DIR):
		print("Project folder not found. Please download the project first.")
		return

	# Create Virtual Environment
	print("Creating the virtual environment")
	run_command(["python3","-m","venv",VENV_DIR])
	print("Virtual environment created.")

	# Activete Virtual Environment and install requirements
	pip_path = os.path.join(VENV_DIR, "bin", "pip")
	requirements_file = os.path.join(DOWNLOAD_DIR,"requirements.txt")

	if os.path.exists(requirements_file):
		print("Installing requirements...")
		run_command([pip_path, "install", "-r", requirements_file])
		print("Requirements installed successfully.")
	else:
		print("requirements.txt not found.")


		

###    START FUNCTION   ###
def start_app():
	if not os.path.exists(VENV_DIR):
		print("Virtual environment not found. Please run the install command first.")
		return

###    RESTART FUNCTION    ###
def restart_app():
	"""Restarts the Flask application"""
	print("Restartin the Flask application...")
	start_app() # starts app again
	# restart logic : stop/start


###    MAIN CLI LOGIC    ###
def main():

	parser = argparse.ArgumentParser(description="Welcome To Hislilogger !!")
	parser.add_argument("-a",action="store_true",help="Automated Installation")
	parser.add_argument("-d","--download",action="store_true",help="Download the project from GitHub")
	parser.add_argument("-i","--install",action="store_true",help="Install the application requirements")
	parser.add_argument("-s","--start",action="store_true",help="Start the Flask application")
	parser.add_argument("-r","--restart",action="store_true",help="Restart the Flask application")

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









