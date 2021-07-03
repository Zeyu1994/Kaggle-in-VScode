# This script is for checking the git and dvc status of code and data.
# Before each mlflow run start, we should make sure that we have committed all the change of code and data.
# If dva doesn't provde python api, write a script 

import git
import dvc.api