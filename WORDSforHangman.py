words = ["apple", "banana", "cherry", "orange", "grape", "strawberry"]

with open("word_library.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
