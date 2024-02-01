import subprocess
def start_service():
    try:
        subprocess.run("sudo systemctl start ids-api", shell=True, check=True)
        print(f"\033[32mCommand executed successfully ! API is launched\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[31mError during command execution : \033[0m{e}")