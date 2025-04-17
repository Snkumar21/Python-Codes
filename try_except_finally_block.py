# Example of finally block exception in python...

try:
    num = 10
    denom = 0
    result = num/denom
    print(result)
except:
    print("Denominator cannot be 0")
finally:
    print("This is finally block")