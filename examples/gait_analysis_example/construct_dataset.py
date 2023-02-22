
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import glob, os
from poser.patients import Patient, PatientCollection
import re

import scipy.stats as st

import seaborn as sns


#%% load in mice labels

folder = './data/'

#%% load patient data


fs = 160


patients = []
patient_groups = []

for file in os.listdir(folder):
    if file.endswith(".csv"):   
        
        print(file)
     
        # getting patient details
        info = re.findall(r'\d+',file)
                
        patient_id = int(info[0])
        speed = int(info[1])
                           
        pose_estimation = pd.read_csv(folder+ '/' +file,header=[1,2])
            
        label = {
                 'speed':speed,
               }

        # get ventral and later columns            
        lat_columns = []
        ventral_columns = []            
        for col in pose_estimation.columns:
            if 'lat' in col[0]:
                lat_columns.append(col[0])
            elif 'ventral' in col[0]:
                ventral_columns.append(col[0])  

        # getting a scaling factor
        sf = abs(pose_estimation[('snout ventral','x')] - pose_estimation[('TB ventral','x')]).median()   
        
        if pose_estimation.shape[0]>100:
            p = Patient(pose_estimation,
                            fs,
                            patient_id=file,
                            label=label,
                            label_name=None,                                
                            low_cut=0,
                            high_cut=10,
                            likelihood_cutoff=0,
                            normalize=True,
                            scaling_factor=1,                                    
                            interpolate_pose=True,
                            )
            patients.append(p)


                       



#%% collect all patients into a collection object

pc = PatientCollection()
pc.add_patient_list(patients)
print("We have {} patients".format(len(pc)))

#%% define structural features to compute

from poser.structural_features import StructuralFeatures

sf = StructuralFeatures(markers = pc.markers)
sf.load_structural_features('structural_feature_files',folder = './')

#%% extract features

from poser.extraction import extract
pc = extract(pc, sf,normalize_features=False)


#%% aggregate features


from poser.feature_aggregation import aggregate
features_df= aggregate(pc,use_dummies=False,compute_advanced=False)

