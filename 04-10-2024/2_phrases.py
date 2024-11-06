def add_excitement(words):
    
    for i in range(len(words)):
        words[i] += "!"

phrases = ["Hello", "Goodbye", "Morning"]
add_excitement(phrases)
print(phrases)