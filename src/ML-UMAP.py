import umap
import numpy

data = []


# build the tsne model on the image vectors
print('building umap model')
reducer = umap.UMAP()
fit_model = reducer.fit_transform(numpy.array(data))
