import numpy as np
y_true = np.array([0.30,0.7,1,0,0.5])
y_predicted = np.array([1,1,0,0,1])
# find mean squared error
total_error = 0
for yt,yp in zip(y_true,y_predicted):
        total_error+=((yt-yp)**2)
print(total_error)
print(f'Mean squared Error:{total_error/y_true.shape}')

# MSE using numpy
MEA = np.mean(np.square(y_true-y_predicted))
print(MEA)

