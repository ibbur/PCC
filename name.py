name = "ada lovelace"
print(name.title())

    # A method (i.e., title) is an action that Python can perform on a piece of data. The (.) after name in name.title() tells Python to make the title() method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work.
    # title() displays each word in titlecase, where each word begins with a capital letter.

print(name.upper())
print(name.lower())

first_name ="ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name + " COMBINED")

print("Hello, " + full_name.title() + "!")

message = ("Hello, " + full_name.title() + "!")
print(message + " VARIABLE")

    # \t adds a tab of whitespace
    # \n adds a return

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

    # The method rstrip() removes whitespace from the right of a string

favorite_language = '1 python '
print(favorite_language + "|")
print (favorite_language.rstrip() + "|")
print(favorite_language + "|")

favorite_language = '2 python '
favorite_language = favorite_language.rstrip()
print(favorite_language + "|")
print(favorite_language + "|")

    # The method lstrip() removes whitespace from the right of a string
    # The method strip() removes whitespace from both the right and left of a string

favorite_language = ' 3 python '
print(favorite_language.rstrip() + "|")
print(favorite_language.lstrip() + "|")
print(favorite_language.strip() + "|")
