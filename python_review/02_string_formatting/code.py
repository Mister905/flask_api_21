name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")

guest = "Tom"
greeting = "Hello, {guest}".format(guest=guest)

print(greeting)

longer_phrase = "Hello, {}. Today is {}."

print(longer_phrase.format("Rolf", "Monday"))