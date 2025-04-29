import numpy as np
import matplotlib.pyplot as plt

# Generating data
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])
y = np.array([0,0,0,1])

# Adding intercept term (bias)
X_b = np.c_[np.ones((X.shape[0], 1)), X]
# 3. Sigmoid
def sigmoid(z):
    return 1/(1+np.exp(-z))

# 4. Cost function (binary cross-entropy)
def compute_cost(X,y, weights):
    m = len(y)
    h = sigmoid(X.dot(weights))
    cost = (- y *np.log(h+1e-15) - (1-y)*np.log(1-h+1e-15)).mean()
    return cost

# 5. Gradient Descent
def train(X,y,lr=0.1, iterations=1000):
    weights = np.zeros(X.shape[1])
    cost_history = []

    for i in range(iterations):
        z = X.dot(weights)
        h = sigmoid(z)
        gradient = X.T.dot(h-y) / y.size
        weights -= lr*gradient

        cost = compute_cost(X,y,weights)
        cost_history.append(cost)

        if i%100==0:
            print(f"Iteration {i}: Cost {cost:.4f}")
        return weights, cost_history

# 6. train the model
weights, cost_history = train(X_b, y)

# 7. Visualize results

plt.figure(figsize=(10,4))

# Subplot 1: Data + Decision Boundary
plt.subplot(1,2,1)
plt.title("Logistics Regression Decision Boundary")
plt.scatter(X[:,0],X[:,1], c=y, cmap="bwr",edgecolors='k',s=100)

# Decision Boundary
x_vals = np.array([0,1])
# Decision boundary line: w0 + w1*x1+w2*x2 = 0 => x2
y_vals = -(weights[0] + weights[1] * x_vals)/weights[2]
plt.plot(x_vals,y_vals, 'k--')
plt.xlabel("x1")
plt.ylabel("x2")
# Subplot 2: Cost function over iterations
plt.subplot(1, 2, 2)
plt.title("Cost Over Iterations")
plt.plot(cost_history)
plt.xlabel("Iteration")
plt.ylabel("Cost")

plt.tight_layout()
plt.show()
