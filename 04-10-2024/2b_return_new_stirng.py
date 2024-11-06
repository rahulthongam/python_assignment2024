new_list=[]
def add_excitement(words):
    for word in words:
        new_list.append(word +"!")


phrases = ["Hello", "Goodbye", "Wow"]
new_phrases = add_excitement(phrases)
print("Original list:", phrases)
print("New list:", new_list)

