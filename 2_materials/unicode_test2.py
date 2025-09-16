with open("test_852.txt") as infile:
    test_string = infile.read()

print("Length:", len(test_string))
for c in test_string:
    print(c, ord(c))
