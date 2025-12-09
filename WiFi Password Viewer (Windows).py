import subprocess

data = subprocess.check_output("netsh wlan show profiles").decode()
profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]

for p in profiles:
    info = subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear").decode()
    print(info)
