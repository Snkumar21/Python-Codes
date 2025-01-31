# Example: Controlled loop to avoid an infinite loop
count = 0

while True:  # Infinite loop with a break condition
    print(f"Current count is: {count}")
    count += 1
    
    # Prevent infinite loop by breaking after a condition is met
    if count == 5:
        print("Breaking the loop to prevent it from being infinite.")
        break