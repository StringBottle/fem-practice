#%%
import numpy as np

# Define stiffness matrix 
k1 = np.array([[200,-200,0, 0],[-200,200,0, 0],[0,0,0, 0], [0, 0, 0, 0]], dtype=float)
k2 = np.array([[0,0,0, 0], [0,200,-200,0],[0,-200,200, 0], [0,0,0, 0]], dtype=float)
k3 = np.array([[0,0,0, 0], [0,0,0, 0], [0, 0, 200,-200],[0, 0, -200,200]], dtype=float)

# Assemble stiffness matrix 
K = k1 + k2 + k3


U = np.array([0, np.nan, np.nan, np.nan], dtype=float)
# Define external force matrix  

F = np.array([np.nan, -5, 0, 20], dtype = float)
#%%


#%%

"""
Solve Equation only with known external forces 
"""

reduce_idx = np.argwhere(np.isnan(F))
F_reduced = np.delete(F, reduce_idx, axis = 0)
K_reduced = np.delete(K, reduce_idx, axis = 0) 
K_reduced = np.delete(K_reduced, reduce_idx, axis = 1) 


U_reduced = np.linalg.solve(K_reduced, F_reduced[:, np.newaxis])
#%%

U[np.isnan(U)] = np.squeeze(U_reduced)


F = K.dot(U)
print ('F1=',F[0],'F2=',F[1],'F3=',F[2])



#%%


f2 = np.array([0])
f3 = np.array([2.5])

f23 = np.array([f2,f3])
k23 = np.array([[200,-100],[-100,100]])

u23 = np.linalg.solve(k23,f23)

u1 = np.array([0])
u2 = u23[0]
u3 = u23[1]

u = np.array([u1,u2,u3])


F = K.dot(u)
print ('F1=',F[0],'F2=',F[1],'F3=',F[2])

# F = np.array([[1],[2],[3]])
# F1 = F[[0]]
# F2 = F[[1]]
# F3 = F[[2]]

# u = np.array([[1],[2],[3]])
# u1 = u[[0]]
# u2 = u[[1]]
# u3 = u[[2]]





# %%
