import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    calculations = {}
    keys = ['mean','variance','standard deviation','max','min','sum']
    calculations = {key: [] for key in keys}
    array = np.array(list)
    matrix = np.reshape(array,(3,3))
    for i in range(2):
        calculations['mean'].append(matrix.mean(axis = i).tolist())
        calculations['variance'].append(np.var(matrix,axis = i).tolist())
        calculations['standard deviation'].append(np.std(matrix,axis = i).tolist())
        calculations['max'].append(matrix.max(axis = i).tolist())
        calculations['min'].append(matrix.min(axis = i).tolist())
        calculations['sum'].append(matrix.sum(axis = i).tolist())
    calculations['mean'].append(float(array.mean()))
    calculations['variance'].append(float(np.var(array)))
    calculations['standard deviation'].append(float(np.std(array)))
    calculations['max'].append(int(array.max()))
    calculations['min'].append(int(array.min()))
    calculations['sum'].append(int(array.sum()))
    return calculations