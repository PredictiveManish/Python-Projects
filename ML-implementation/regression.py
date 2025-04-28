## Implementing Linear regression from basics
"""
1. Sample data
2. Calculating X' and Y'
3. Calculating numerator and denominator for slope
4. Compute slope m
5. Compute Intercept c
6. Write the function to predict y for any given x.
7. Measuring error for valuation"""
X = [140,155,159,179,192,210]
Y = [60,62,67,70,71,72]
# Mean calculation
X_sum = 0
Y_sum = 0
for i in X:
    X_sum += i
    X_mean = X_sum/len(X)
for j in Y:
    Y_sum += j
    Y_mean = Y_sum/len(Y)

numerator_sum =0
denominator_sum = 0
for i in range(len(X)):
    numerator_sum += (X[i]-X_mean) * (Y[i]- Y_mean)
    denominator_sum += (X[i]- X_mean) * (X[i]-X_mean)
slope_m = numerator_sum/denominator_sum

intercept = Y_mean - slope_m * X_mean

y_pred = []
for x in X:
    y = slope_m*x + intercept
    y_pred.append(y)

print(y_pred)

min_X, max_X = min(X), max(X)
min_Y, max_Y = min(Y), max(Y)

graph_width = 50
graph_length = 20

grid = [[' ' for _ in range(graph_width+1)] for _ in range(graph_length+1)]
for i in range(len(X)):
    scaled_X = int((X[i]- min_X)/(max_X-min_X)*graph_width)
    scaled_Y = int((Y[i]-min_Y)/(max_Y-min_Y)*graph_length)
    scaled_Y = graph_length - scaled_Y
    if 0<= scaled_Y<=graph_length and 0 <=scaled_X <=graph_width:
        grid[scaled_Y][scaled_X] = '*'
for row in grid:
    print(''.join(row))