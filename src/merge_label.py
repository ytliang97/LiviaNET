import argparse
import timeit

import nibabel as nib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

nib.Nifti1Header.quaternion_threshold = -1e-06

parser = argparse.ArgumentParser()
parser.add_argument('--label_path', help='nifti data path. (.nii)')
parser.add_argument('--roi_path', help='nifti data path. (.nii)')
FLAGS = parser.parse_args()

label = nib.load(FLAGS.label_path)
roi = nib.load(FLAGS.roi_path)
#print(type(label))

label_arr = label.get_data()
roi_arr = roi.get_data()
#print(type(label_arr))

print('label of ',FLAGS.label_path.split('/')[-1], ':', np.unique(label_arr))
print('total', len(np.unique(label_arr)))
print('shape', label_arr.shape)

print('label of ',FLAGS.roi_path.split('/')[-1], ':', np.unique(roi_arr))
print('total', len(np.unique(roi_arr)))
print('shape', roi_arr.shape)

start = timeit.default_timer()
for i in range(roi_arr.shape[0]):
    for j in range(roi_arr.shape[1]):
        for k in range(roi_arr.shape[2]):
            if label_arr[i,j,k] == 0 and roi_arr[i,j,k] == 1:
                label_arr[i,j,k] = 1
print('process time:',timeit.default_timer()-start)

new_label = nib.Nifti1Image(label_arr, label.affine)
new_label_path = FLAGS.label_path[:-4] + 'm.nii'
nib.save(new_label, new_label_path)



