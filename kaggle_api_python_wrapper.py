import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_dataset(competition : str, targetpath = None):
    if targetpath is None:
        targetpath = os.getcwd() + f"/dataset/{competition}"
        print(f"target dataset path is: {targetpath}")
        try:
            os.makedirs(targetpath)
        except OSError:
            print("dirs already existed")
    api = kaggle_access()
    # todo: check if file exits or not
    api.competition_download_files(competition, path = targetpath)
    
    with zipfile.ZipFile(targetpath+f'/{competition}.zip' , 'r') as zip_ref:
        zip_ref.extractall(targetpath)
    os.remove(targetpath+f'/{competition}.zip')
    return



    

def kaggle_access():
    api = KaggleApi()
    try:
        api.authenticate()
    except:
        print("Please setup your kaggle Token")
    return api