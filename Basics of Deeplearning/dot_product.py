import numpy as np
price_per_unit = np.array([20,30,15])
sold_goods = np.array([[50,60,25],
                        [10,13,5],
                        [40,70,52]])
# Let's find the total prices using dot product
total_price = np.dot(price_per_unit,sold_goods)
print(total_price) 