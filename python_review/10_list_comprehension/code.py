numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.lower().startswith("s"):
        starts_s.append(friend)

print(starts_s)