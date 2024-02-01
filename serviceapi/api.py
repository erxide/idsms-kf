from pathlib import Path
import subprocess
from serviceapi.ask_user import ask_username


def create_service():
    WorkingDirectory = f'{Path("ids-api.py").resolve().parent}'
    cmd = f'/bin/python {Path("ids-api.py").resolve()} r'
    path = "/lib/systemd/system/ids-api.service"
    confidsservice = f'[UNIT]\nDescription=ids-api service\n\n[Service]\nType=simple\nRestart=always\nRestartSec=5s\nUser={ask_username()}\nWorkingDirectory={WorkingDirectory}\nExecStart={cmd}\n\n[Install]\nWantedBy=multi-user.target\n'
    try:
        with open(path, 'w') as f:
            f.write(confidsservice)
    except OSError as e:
        print('Error : ', e)

    commands = [
        "sudo systemctl daemon-reload",
        "sudo systemctl enable ids-api.service"
    ]

    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"\033[32mCommand \033[0m{command}\033[32m executed successfully !\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"\033[31mError during command execution : \033[0m{e}")