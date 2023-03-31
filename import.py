import subprocess
import os
import shutil

# Set the name of the input file
input_file = 'environments.zip'

# Unpack the input file
shutil.unpack_archive(input_file)
print(f'Unpacked {input_file}')

# Set the name of the input directory
input_dir = 'environments'

# Loop through each file in the input directory and import it
for file in os.listdir(input_dir):
    # Set the name of the environment to create
    env_name = os.path.splitext(file)[0]

    # Set the name of the input file
    input_file = os.path.join(input_dir, file)

    # Run the conda env create command
    print(f'Importing environment: {env_name}')
    subprocess.run(['conda', 'env', 'create', '-n', env_name, '-f', input_file])
