import argparse

import nibabel as nib
import numpy as np

nib.Nifti1Header.quaternion_threshold = -1e-06

parser = argparse.ArgumentParser()
parser.add_argument('--label_path', help='nifti data path. (.nii)')
FLAGS = parser.parse_args()

img = nib.load(FLAGS.label_path)
img = img.get_data()

print('label of ',FLAGS.label_path.split('/')[-1], ':', np.unique(img))
print('total', len(np.unique(img)))
print('shape', img.shape)

print('amount of label 0:',np.count_nonzero(img==0))
print('amount of label 1:',np.count_nonzero(img==1))
print('amount of label 2:',np.count_nonzero(img==2))