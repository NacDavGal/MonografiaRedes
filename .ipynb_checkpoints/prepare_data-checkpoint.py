import os
from random import shuffle
import re
import pdb

def get_files(root, suffix):
    all_files = []
    for parent,_,files in os.walk(root):
        for file in files:
            if re.search(suffix, file):
                all_files.append(os.path.join(parent, file))
    return all_files

def get_file_prefix(file):
    return re.search('(.*/[a-z0-9A-Z_-]*)_[0-9]*.jpg', file).group(1)

def all_dirs_exist(file):
    #buscar las 3 direcciones que quedan _90.jpg, _180.jpg y _270.jpg
    return (os.path.isfile(file + '_0.jpg') and
            os.path.isfile(file + '_90.jpg') and
            os.path.isfile(file + '_180.jpg') and
            os.path.isfile(file + '_270.jpg'))

def group_pictures(root):
    labeled_filenames = []
    all_labels = []
    for dir in os.listdir(root): #Para cada direccion dentro de path
        cur_dir = os.path.join(root,dir) # cur_dir es path\dir
        if os.path.isdir(cur_dir): # Basicamente si existe
            label = dir
            all_labels.append(label)
            # A partir de quedarme con una copia de cada archivo en la base de datos 
            files = [get_file_prefix(file) for file in get_files(dir, '_0.jpg')]
            labeled_filenames = [(extend_dirs(file),len(all_labels)-1) for file in files if all_dirs_exist(files)]
             
    print("Terminé")

#group_pictures("50States2k_test/test_data")