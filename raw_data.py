import numpy as np
np.random.seed(0)

num_vals = 10
x_vals = np.arange(num_vals).reshape(-1, 1)
example_data_10 =  5 + 2 * x_vals + np.random.normal(0, 2, num_vals).reshape(-1, 1)


num_test = 3
x_test = np.arange(num_vals, num_vals+num_test).reshape(-1, 1)
prediction_data_10 = 5 + 2 * x_test + np.random.normal(0, 2, num_test).reshape(-1, 1)
