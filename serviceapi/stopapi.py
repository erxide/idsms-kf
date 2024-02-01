import subprocess

def stop_service():
    try:
        subprocess.run("sudo systemctl stop ids-api", shell=True, check=True)
        print(f"\033[32mCommand executed successfully ! API has been stopped\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[31mError during command execution : \033[0m{e}")