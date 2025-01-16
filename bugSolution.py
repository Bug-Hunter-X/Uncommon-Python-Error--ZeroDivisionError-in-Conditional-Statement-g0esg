def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        return float('inf')  # Or another appropriate handling such as raising a custom exception
        # print("Error: Cannot divide by zero") # alternative