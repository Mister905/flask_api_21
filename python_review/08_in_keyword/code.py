friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

movies_watched = {"The Matrix", "Toy Story", "Amadeus"}

user_movie = input("Enter a movie you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't see it.")

