#hola
import shutil
import pathlib
import os
from pngtojpg import pngtojpg 

def extract_images_from_excel(path, dir_extract=None):
    if type(path) is str:
        path = pathlib.Path(path)
    if dir_extract is None:
        dir_extract = path.parent
    if path.suffix != '.xlsx':
        raise ValueError('path must be an xlsx file')
    name = path.name.replace(''.join(path.suffixes), '') # name of excel file without suffixes
    #temp_file = pathlib.Path(source_file).parent / 'temp.xlsx' # temp xlsx
    temp_file = path.parent / 'temp.xlsx' # temp xlsx
    temp_zip = temp_file.with_suffix('.zip') # temp zip
    #shutil.copyfile(source_file, temp_file)
    shutil.copyfile(path, temp_file)
    temp_file.rename(str(temp_zip))
    extract_dir =  temp_file.parent / 'temp'
    extract_dir.mkdir(exist_ok=True)
    save_dir = path.parent / name
    save_dir.mkdir(exist_ok=True)
    shutil.unpack_archive(temp_zip, extract_dir) # unzip xlsx zip file
    paths_img_png = sorted((extract_dir / 'xl' / 'media').glob('*.[jpeg jpg png]*')) # find images png
    #print(paths_img_png)
    path_converted=[pngtojpg(str(path)) for path in paths_img_png]
    
    move_paths_png = {path: os.path.join(save_dir, str(os.path.basename(pathlib.Path(path).name.replace('image','0'))).zfill(10)) for n, path in enumerate(path_converted)} # create move path dict 
    new_paths = [shutil.move(old, new) for old, new in move_paths_png.items()] # move / rename image files
    
    
    shutil.rmtree(extract_dir) # delete temp folder
    temp_zip.unlink() # delete temp file
    return name



