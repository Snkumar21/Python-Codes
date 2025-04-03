# Example of try-except exception handling in python...

try:
    num = 10
    denom = 0

    divresult = num/denom

    print(divresult)
except:
    print("Denominator cannot be 0")