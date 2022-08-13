# We will implement log function 
import numpy as np
y_true = np.array([1,2,3,4,0])
y_predicted = np.array([1,2,0,3,0])
epsilon = 1e-15

y_predicted_new = [max(i,epsilon) for i in y_predicted]
print(y_predicted_new)
print('after updation of y_predicted_new')
y_predicted_new = [min(i,(1-epsilon)) for i in y_predicted_new]
print(y_predicted_new)
def log_loss(y_true,y_predicted):
    y_predicted_new = [max(i,epsilon) for i in y_predicted]
    y_predicted_new = [min(i,(1-epsilon)) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(y_true*np.log(y_predicted_new)+(1-y_true)*np.log(1-y_predicted_new))
print (log_loss(y_true,y_predicted=y_predicted)) 

