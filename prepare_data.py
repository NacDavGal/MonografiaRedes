import os
from random import shuffle
import re
import pdb

def get_files(cur_dir, regex):
    out_files = []
    for subdir,_,files in os.walk(cur_dir):
        out_files.extend([ os.path.join(subdir, file)
                           for file in files if re.search(regex, file)])

def group_pictures(root):
    labeled_filenames = []
    all_labels = []
    for dir in os.listdir(root):
        cur_dir = os.path.join(root,dir)
        if os.path.isdir(cur_dir):
            label = dir
            all_labels.append(label)
            
        
    print("Terminé")

group_pictures("50States2k_test\\test_data")
