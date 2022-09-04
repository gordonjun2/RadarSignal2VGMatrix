import numpy as np
from PIL import Image as im
from ts2vg import NaturalVG

ts = [1.0, 0.6, 0.5, 0.8, 1.0, 0.5, 0.6, 0.9, 1.0, 0.7, 0.6, 0.9, 1.0, 0.7, 0.6, 1.0]

g = NaturalVG()
g.build(ts)

vg_mat = g.adjacency_matrix(triangle='both')
vg_mat_im_obj = im.fromarray(vg_mat*255)
vg_mat_im_obj.save('vg_mat_test.png')

### Features of Visibility Graph ###

# Average Degree
deg = g.degrees
avg_deg = sum(deg) / len(deg)

# Average Clustering Coefficient

# Newman Coordination Coefficient

# Normalized Network Structure Entropy

# VG Complexity

# VG Density

num_edges = len(g.edges)
