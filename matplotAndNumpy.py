#Simple linear regression using numpy, and visualized with matplotlib.

import matplotlib.pyplot as plt
import numpy as np

X = [173, 171, 189, 181]
Y = [81, 72, 96, 94]

# Add a column of ones for the bias term (intercept)
X_ones = np.c_[np.ones(4), X]

# Calculate the theta parameters using the least squares formula
theta = np.linalg.inv(X_ones.T.dot(X_ones)).dot(X_ones.T).dot(Y)

print("Theta parameters:", theta)

# Create a scatter plot of the data points
plt.scatter(X, Y, s=40, c='#06d6a0')

# Define the limits for the regression line
X_lim = [170, 190]
X_lim_ones = np.c_[np.ones(2), X_lim]

# Calculate predicted Y (weight) values using X limits and theta
Y_lim = X_lim_ones.dot(theta)

# Plot the regression line
plt.plot(X_lim, Y_lim, 'r-')

# Configure plot axes and labels
plt.axis([170, 190, 70, 100])
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height x Weight')
plt.grid()

weight_person = theta[0] + (theta[1] * 195)
print('My guessing:', weight_person)

plt.show()
