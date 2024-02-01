import subprocess
def restart_service():
    try:
        subprocess.run("sudo systemctl restart ids-api", shell=True, check=True)
        print(f"\033[32mCommand executed successfully ! API has been restarted\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[31mError during command execution : \033[0m{e}")