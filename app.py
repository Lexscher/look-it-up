from PyDictionary import PyDictionary

dictionary = PyDictionary()


ans = input("Would you like to look up a word? (y/n) ")

while (ans != "n"):
    # grab query from user
    query = input("Enter a word you're curious about: ")
    # get the meaning of that word
    response = dictionary.meaning(query)
    # print out the results to the user
    print(response.keys())
    for definition in response.values():
        print(definition)
    # ask the user if they'd like to search another word
    ans = input("Would you like to look up another word? (y/n) ")

    while (ans.lower() != 'y' and ans.lower() != 'n'):
        print("That is an invalid input, please try again")
        ans = input("Would you like to look up another word? (y/n) ")
        pass

    pass

print("Goodbye!")
