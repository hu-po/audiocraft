'''
Installation instructions

git clone https://github.com/facebookresearch/audiocraft.git
git remote set-url origin https://github.com/hu-po/audiocraft.git

conda create --name audiocraft --clone simicam
conda activate audiocraft
pip install -e .
pip install huggingface_hub
pip install tensorboardX

Had to install NVCC
https://docs.nvidia.com/deeplearning/nccl/install-guide/index.html#debian

# Does not work...
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt update

# Manual download and install
tar xvf nccl_2.18.3-1+cuda11.0_x86_64.txz
ldconfig -p | grep nccl
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/nccl_2.18.3-1+cuda11.0_x86_64/lib

# Install cuDNN
https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html
sudo dpkg -i cudnn-local-repo-ubuntu2204-8.5.0.96_1.0-1_amd64.deb
sudo apt-get install libcudnn8=8.5.0.*-1+cuda11.7
sudo apt-get install libcudnn8-dev=8.5.0.*-1+cuda11.7
sudo apt-get install libcudnn8-samples=8.5.0.*-1+cuda11.7
'''
import os
from huggingface_hub import snapshot_download

snapshot_download(repo_id="facebook/musicgen-small")
snapshot_download(repo_id="facebook/audiogen-small")
os.environ['AUDIOCRAFT_CACHE_DIR'] = '/home/oop/.cache/huggingface/hub/'