'''
Copyleft Oct 15, 2016 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;

np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;

home = os.path.expanduser('~') + '/'
def mkdir(path):
    if not os.path.exists(path): os.makedirs(path)


from shutil import copyfile


mkdir('PLOS/figures')
pd.read_csv('PLOS/index.figures.txt',header=None).apply(lambda x: copyfile('figures/{}.tiff'.format(x[0]), 'PLOS/figures/Fig{}.tiff'.format(x.name+1)) ,axis=1)
pd.read_csv('PLOS/index.supplfigures.txt',header=None).apply(lambda x: copyfile('figures/{}.tiff'.format(x[0]), 'PLOS/figures/S{}Fig.tiff'.format(x.name+1)) ,axis=1)