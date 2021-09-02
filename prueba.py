#import tensorflow as tf
import numpy as np
import os
import re
from random import shuffle
import pdb


# Utility function for getting all of the training examples in a directory
# datasets have the structure of root/<Sate Name>/<image ID>_<heading>.png

def get_files(cur_dir, regex):
    out_files = []
    for subdir,_,files in os.walk(cur_dir):
        out_files.extend([ os.path.join(subdir, file)
                           for file in files if re.search(regex, file)])
    return out_files

def get_file_prefix(filename):
    return re.search('(.*\\\\[a-z0-9A-Z_-]*)_[0-9]*.jpg', filename).group(1)

def all_directions_exist(prefix):
    return (os.path.isfile(prefix + '_0.jpg') and
            os.path.isfile(prefix + '_90.jpg') and
            os.path.isfile(prefix + '_180.jpg') and
            os.path.isfile(prefix + '_270.jpg'))

def prefix_to_filenames(prefix):
    return (prefix + '_0.jpg', prefix + '_90.jpg', prefix + '_180.jpg',
            prefix + '_270.jpg')

def read_grouped_filenames_and_labels(root):
    labeled_filenames = []
    all_labels = []
    for dir in os.listdir(root):
        cur_dir = os.path.join(root, dir)
        if os.path.isdir(cur_dir):
            label = dir
            all_labels.append(label)
            file_prefixes = [ get_file_prefix(file) for file in get_files(cur_dir, '_0.jpg') ]
            cur_files = [ prefix_to_filenames(prefix) for prefix in file_prefixes
                          if all_directions_exist(prefix) ]
            labeled_filenames.extend([ (filenames, len(all_labels)-1)
                                       for filenames in cur_files ])
    files = [ tmp[0] for tmp in labeled_filenames ]
    labels = [ tmp[1] for tmp in labeled_filenames ]

    return files,labels, all_labels

files, labels, all_labels = read_grouped_filenames_and_labels("50States2k_test\\test_data")

n = 13299
print(f"El archivo es : {files[n]} ")
#print(files[n])
print(f"Y está en {all_labels[labels[n]]}")
#print(all_labels[labels[n]])

#m = re.search('((?:[^\\]*\\)*).*.jpg', '50States2k_test\\test_data\\Alabama\\2007_-AQOXlx5fs1gPSRBUftj5w_0.jpg')
#print(m)

#n = re.search('(.*\\\\[a-z0-9A-Z_-]*)_[0-9]*.jpg','ricardo\\tuculo\\tuvieja_08.jpg')

#print("La segunda oracion queda: ")
#print(n.group(1))