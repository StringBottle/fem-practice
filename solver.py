
#%%
"""
Solver 1. 
Solve Equation only with known external forces 
"""

reduce_idx = np.argwhere(np.isnan(F))
F_reduced = np.delete(F, reduce_idx, axis = 0)
K_reduced = np.delete(K, reduce_idx, axis = 0) 
K_reduced = np.delete(K_reduced, reduce_idx, axis = 1) 

U_reduced = np.linalg.solve(K_reduced, F_reduced[:, np.newaxis])
U[np.isnan(U)] = np.squeeze(U_reduced)


F = K.dot(U)


#%%
"""
Solver 2. 
Solve equation when external force given by specified displacement
"""
unknown_idx_u = np.argwhere(np.isnan(U))
known_idx_u = np.argwhere(~np.isnan(U))

unknown_idx_f = np.argwhere(np.isnan(F))
known_idx_f = np.argwhere(~np.isnan(F))
#%%
K_ruu = np.delete(K, unknown_idx_u, axis = 1) # ruu : reduce unknown displacement idx 
K_ruu_ruf = np.delete(K_ruu, unknown_idx_f, axis = 0) # ruf : reduce unknown force idx

K_rku = np.delete(K, known_idx_u, axis = 0) # ruu : reduce known displacement idx 
K_rku_rku = np.delete(K_rku, known_idx_u, axis = 1) # ruu : reduce known displacement idx 
U_ruu = np.delete(U, unknown_idx_u, axis = 0) # ruu : reduce unknown displacement idx 

temp = K_ruu_ruf.dot(U_ruu)
F_ruf = np.delete(F, unknown_idx_f, axis = 0) # ruu : reduce unknown force idx 
U_rku_rku = np.linalg.solve(K_rku_rku, F_ruf - temp )
U[unknown_idx_u] = U_rku_rku[:, np.newaxis]

F = K.dot(U)