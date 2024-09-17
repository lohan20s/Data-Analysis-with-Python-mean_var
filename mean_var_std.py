import numpy as np

def calculate(list):
    #input should be a list of 9 digits
    if len(list)<9:
      raise ValueError("List must contain nine numbers.")
   
    #reshape the list into a 3X3 matrix 
    reshaped_list=np.reshape(list,[3,3])
      
    #return a dictionary with mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in matrix
    calculations={"mean":[np.mean(reshaped_list,axis=0,dtype=np.float64).tolist(), np.mean(reshaped_list,axis=1,dtype=np.float64).tolist(), np.mean(list,dtype=np.float64)],
                  "variance":[np.var(reshaped_list,axis=0,dtype=np.float64).tolist(), np.var(reshaped_list,axis=1,dtype=np.float64).tolist(), np.var(list,dtype=np.float64)],
                  "standard deviation":[np.std(reshaped_list,axis=0,dtype=np.float64).tolist(), np.std(reshaped_list,axis=1,dtype=np.float64).tolist(), np.std(list,dtype=np.float64)],
                   "max":[np.max(reshaped_list,axis=0).tolist(), np.max(reshaped_list,axis=1).tolist(), np.max(list)],
                   "min":[np.min(reshaped_list,axis=0).tolist(), np.min(reshaped_list,axis=1).tolist(), np.min(list)], 
                   "sum":[np.sum(reshaped_list,axis=0).tolist(), np.sum(reshaped_list,axis=1).tolist(), np.sum(list)]}

    return calculations