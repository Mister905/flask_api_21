users = [
    (0, "Bob", "password"),
    (1, "Example2", "example2"),
    (2, "Example3", "example3"),
    (3, "Example4", "example4"),
]

# user[1]: user => key: value 
username_mapping = {user[1]: user for user in users}

print(username_mapping["Bob"])