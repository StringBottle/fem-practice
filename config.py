#%%
import numpy as np

# Define stiffness matrix 

# Define elements as follow : 
# Option 1. [start node, end node, stiffness]
# Option 2. [start node, end node, elasticity, area, length]
# Option 3. [start node, end node, elasticity, area, length, theta]


num_nodes = 3

elements = [
    {'start_node' : 1, 'end_node' : 2, 'E': 210, 'A': 4*10**(-4), 'L': 1},
    {'start_node' : 2, 'end_node' : 3, 'E': 210, 'A': 4*10**(-4), 'L': 1} 
] 

#TODO : replace np.nan with more intuitive variable name 
forces = [
    np.nan, 0, -10, 
]

displacements = [
    0, np.nan, np.nan, 
]