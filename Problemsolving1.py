def find_village_name(villagers):
    # Take the first name as base
    prefix = villagers[0]

    # Check prefix with all other names
    for name in villagers[1:]:
        while not name.startswith(prefix):
            prefix = prefix[:-1]  # reduce prefix
            if prefix == "":
                return ""  # no common village name
    return prefix

# Example
villagers = input("Enter villagers' names separated by space: ").split()
print("Village Name:", find_village_name(villagers))