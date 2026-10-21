import mean_var_std

# Test your calculate function
try:
    result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
except ValueError as e:
    print(e)