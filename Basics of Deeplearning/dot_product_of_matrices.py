import numpy as np
# 1US doller = 75 INR
revenues = np.array([[200,220,250],
[68,79,105],
[110,140,180],
[80,85,90]])
print(type(revenues))
print(revenues)
INR_revenues = 75 * revenues
print('Revenues in indian Rupees')
print(INR_revenues)