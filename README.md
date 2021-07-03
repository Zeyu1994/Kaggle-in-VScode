# Kaggle-in-VScode
## Getting started
### 1. Choose a image to build
Kaggle kernel image is not updated in Docker hub.

1. Pull from google container:
   * CPU-only: gcr.io/kaggle-images/python
   * GPU: gcr.io/kaggle-gpu-images/python
2. Build by github: https://github.com/Kaggle/docker-python

### 2. Edit your devcontainer.json
1. Generate your kaggle key at your kaggle homepage.
2. Add the key into *.devcontainer_format.json* and rename it as *.*devcontainer.json*
   * See more tips [here](https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files)
3. Build the container in VScode.