import os
import subprocess

output = subprocess.check_output("conda env list", shell=True).decode()
lines = output.strip().split('\n')
for line in lines:
    if line.startswith('#'):
        continue
    name = line.split()[0]
    if name != 'base':
        print(f"Exporting environment: {name}")
        os.system(f"conda activate {name} && conda env export > {name}.yml")
