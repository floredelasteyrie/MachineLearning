from numpy import *
import matplotlib.pyplot as plt
import scipy.optimize as op

from computeCost import computeCost
from computeGrad import computeGrad
from predict import predict

from sklearn.model_selection import train_test_split
 
# Load the dataset
# The first two columns contains the exam scores and the third column
# contains the label.
data = loadtxt('data1.txt', delimiter=',')
X = data[:, 0:2]
y = data[:, 2]

X, X_test, y, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Plot data 
pos = where(y == 1) # instances of class 1
neg = where(y == 0) # instances of class 0
plt.scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
plt.scatter(X[neg, 0], X[neg, 1], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Admitted', 'Not Admitted'])
plt.show()

#Add intercept term to X
X_new = ones((X.shape[0], 3))
X_new[:, 1:3] = X
X = X_new

# Initialize fitting parameters
initial_theta = zeros((3,1))

# Run minimize() to obtain the optimal theta
Result = op.minimize(fun = computeCost, x0 = initial_theta, args = (X, y), method = 'TNC',jac = computeGrad);
theta = Result.x;
print(theta)

# Plot the decision boundary
plot_x = array([min(X[:, 1]) - 2, max(X[:, 2]) + 2])
plot_y = (- 1.0 / theta[2]) * (theta[1] * plot_x + theta[0])
plt.plot(plot_x, plot_y)
plt.scatter(X[pos, 1], X[pos, 2], marker='o', c='b')
plt.scatter(X[neg, 1], X[neg, 2], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Decision Boundary', 'Admitted', 'Not Admitted'])
plt.title('Training Set')
plt.show()

# Compute accuracy on the training set
p = predict(array(theta), X)
counter = 0
for i in range(y.size):
    if p[i] == y[i]:
        counter += 1
print 'Train Accuracy on training set: %f' % (counter / float(y.size) * 100.0)


# Plot and Compute accuracy on the test set

X_new = ones((X_test.shape[0], 3))
X_new[:, 1:3] = X_test
X_test = X_new

pos = where(y_test == 1) # instances of class 1
neg = where(y_test == 0) # instances of class 0
plot_x = array([min(X_test[:, 1]) - 2, max(X_test[:, 2]) + 2])
plot_y = (- 1.0 / theta[2]) * (theta[1] * plot_x + theta[0])
plt.plot(plot_x, plot_y)
plt.scatter(X_test[pos, 1], X_test[pos, 2], marker='o', c='b')
plt.scatter(X_test[neg, 1], X_test[neg, 2], marker='x', c='r')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
plt.legend(['Decision Boundary', 'Admitted', 'Not Admitted'])
plt.title('Test Set')
plt.show()

p = predict(array(theta), X_test)
counter = 0
for i in range(y_test.size):
    if p[i] == y_test[i]:
        counter += 1
print 'Train Accuracy on test set: %f' % (counter / float(y_test.size) * 100.0)
