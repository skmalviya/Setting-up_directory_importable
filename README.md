## Help Links :

## Setting-up a directory as an importable library (Making a custom environment in gym)
 (https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa)

**Setup libraries:**

* sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
* pip install virtualenv
* virtualenv --python=python3 openai_env
* source openai_env/bin/activate
* pip install tensorflow==1.14
* git clone https://github.com/openai/baselines.git
* cd baselines
* python setup.py install
* Followed link to install https://github.com/openai/mujoco-py
    * Download the MuJoCo version 2.0 binaries for Linux or OSX.
    * Unzip the downloaded mujoco200 directory into ~/.mujoco/mujoco200
    * write https://github.com/MahanFathi/iLQG-MuJoCo/blob/master/bin/mjkey.txt to /home/.mujoco/
    * export LD_LIBRARY_PATH=/home/shrikant/.mujoco/mujoco200/bin:$LD_LIBRARY_PATH
    * sudo apt-get install libglew-dev
    * sudo apt-get install patchelf
    * sudo apt install libosmesa6-dev libosmesa6 libglapi-mesa
    * sudo apt-file search "GL/osmesa.h"
    * sudo apt install --reinstall build-essential & cmake
    * sudo apt install --reinstall libgl1-mesa-dev
    * (may not be required.)sudo apt install --reinstall libgl1-mesa-glx
    * sudo ln -s /usr/lib/x86_64-linux-gnu/libGL.so.1 /usr/lib/libGL.so
    * pip install -U 'mujoco-py<2.1,>=2.0'
* pip install pytest
* python -m baselines.run --alg=deepq --env=PongNoFrameskip-v4 --num_timesteps=1e6

**Running the code:**
```
# After following the instructions and making the custom library.
cd Ashish_poddar_cust_env
pip install -e .
# import using:
from gym_silpa.envs.silpa_env import SilpaEnv
```
