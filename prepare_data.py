import os
from random import shuffle
import re
import pdb

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
