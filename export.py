import subprocess
import os
import shutil

# Set the name of the output directory
output_dir = 'environments'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the list of all conda environments
result = subprocess.run(['conda', 'env', 'list', '--json'], stdout=subprocess.PIPE)
envs = result.stdout.decode('utf-8')

# Loop through each environment and export it
for env in envs:
    # Skip the base environment
    if env == 'base':
        continue

    # Set the name of the output file
    output_file = os.path.join(output_dir, f'{env}.yml')

    # Run the conda env export command
    print(f'Exporting environment: {env}')
    subprocess.run(['conda', 'env', 'export', '-n', env, '--no-build', '-f', output_file])

# Package the exported yml files
shutil.make_archive('environments', 'zip', output_dir)
print(f'Packaged environments into environments.zip')
