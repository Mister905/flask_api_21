def add(x, y):
    print(x+y)

add(4, 4)

# Postional Args
def say_hello(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
    
say_hello("James", "McCarthy")

# Named args
say_hello(last_name="McCarthy", first_name="James")
