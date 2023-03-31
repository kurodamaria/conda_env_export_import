import subprocess
import os
import shutil
import json

# Set the name of the output directory
output_dir = 'environments'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the list of all conda environments
result = subprocess.run(['conda', 'env', 'list', '--json'], stdout=subprocess.PIPE)
envs = json.loads(result.stdout.decode('utf-8'))['envs']

# Loop through each environment and export it
for env in envs:
    # Skip the base environment
    if env.endswith('anaconda3'):
        continue

    # Get the name of the environment
    env_name = os.path.basename(env)

    # Set the name of the output file
    output_file = os.path.join(output_dir, f'{env_name}.yml')

    # Run the conda env export command
    print(f'Exporting environment: {env_name}')
    subprocess.run(['conda', 'env', 'export', '-n', env_name, '--no-build', '-f', output_file])

# Package the exported yml files
shutil.make_archive('environments', 'zip', output_dir)
print(f'Packaged environments into environments.zip')
