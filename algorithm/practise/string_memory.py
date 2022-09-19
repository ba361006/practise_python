keyword_list = ["Life", "is", "short", ",", "I", "use", "Python"]

context = ""
for keyword in keyword_list:
    # this will create multiple objects
    context += keyword + " "
    print(id(context), context)

# this create only one
print(" ".join(keyword_list))