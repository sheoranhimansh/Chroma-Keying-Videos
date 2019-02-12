import warnings; warnings.filterwarnings('ignore');

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.misc import imread

import skimage
from skimage import img_as_ubyte
from skimage.transform import rescale
from skimage.transform import rotate
from skimage import io
from skimage import filters
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank

#File where to save the final image of this document
output_filename = 'outfile.png'
bg = imread('bg.png', mode='RGBA')
fg = imread('fg.jpg', mode='RGBA')
