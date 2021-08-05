import numpy as np


def assemble_stiff_mat(num_nodes, elements):
    
    """Assemble stiffness matrix 

    Args : 
        num_nodes (int) : number of nodes 
        elements (list) : list of each element dictionary

    Return 
        K (np.array, float) : stiffness matrix 
    
    """
    K = np.zeros((num_nodes, num_nodes), dtype = float)

    for elem in elements : 
        print(elem)
        
        K_temp = np.zeros((num_nodes, num_nodes), dtype = float)

        start_node, end_node, stiffness = parse_stiff_dict(elem)
        print(start_node, end_node, stiffness)

        K_temp[start_node, start_node] = stiffness
        K_temp[start_node, end_node] = -stiffness
        K_temp[end_node, start_node] = -stiffness
        K_temp[end_node, end_node] = stiffness

        K += K_temp

    return K 


def parse_stiff_dict(element):
    """Parse stiffness dictionary 

    Args : 
        element (dict) : element dictionary defined in configuration file 
    
    Return : 
        start_node (int)
        end_node (int)
        stiffness (int or float) 

    Variables : 
        E (int or float) : elasticity 
        A (int or float) : area
        L (int or float) : length
    """
    
    start_node = element.get('start_node', None)
    end_node = element.get('end_node', None)
    stiffness = element.get('stiffness', None)
    E = element.get('E', None)
    A = element.get('A', None)
    L = element.get('L', None)

    print(E, A, L )

    if start_node and end_node : 
        # the node notation starts from 1 
        start_node -= 1
        end_node -= 1

    if not stiffness : 
        # suppose the element is truss element
        stiffness = E*A/L

    return start_node, end_node, stiffness 
