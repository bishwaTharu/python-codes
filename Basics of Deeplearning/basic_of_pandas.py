import pandas as pd
import numpy as np
cov = np.array([[6, -3], [-3, 3.5]])
pts = np.random.multivariate_normal([0, 0], cov, size=800)
print(pts.shape)

import matplotlib.pyplot as plt
plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
plt.title('Multivarite Normal Distribution')
plt.axis('equal')
plt.grid()
plt.show() 
