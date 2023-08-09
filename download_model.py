'''
git remote set-url origin https://github.com/hu-po/audiocraft.git
'''
import os
from huggingface_hub import snapshot_download

snapshot_download(repo_id="facebook/musicgen-medium")
snapshot_download(repo_id="facebook/audiogen-medium")
os.environ['AUDIOCRAFT_CACHE_DIR'] = 'ls /home/oop/.cache/huggingface/hub/'