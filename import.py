import glob
import os

for file in glob.glob('*.yml'):
    name = os.path.splitext(file)[0]
    print(f"Creating environment: {name}")
    os.system(f"conda env create -f {file} -n {name}")
