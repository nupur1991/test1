import numpy as np
import math
import cv2
import tensorflow as tf
from sklearn.utils import shuffle
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sklearn

### Read the csv
import os
import csv

sim_data_set = []
csv_path = './data/driving_log.csv'
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        sim_data_set.append(line)
#From csv file, first line is header, so remove header line
sim_data_set = sim_data_set[1:]
print('Data import done!')

