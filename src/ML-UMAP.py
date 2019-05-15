import json
import umap
import numpy as np
import glob
import matplotlib.pyplot as plt


# create datastores
data = [a, b, c, d, e]


# build the tsne model on the image vectors
print('building umap model')
reducer = umap.UMAP()
fit_model = reducer.fit_transform(np.array(data))
