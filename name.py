name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

name = "ada lHHovelace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("\tPython")
print("Language:\nPython\nC\nJavascript")
print("Language:\n\tPython\n\tC\n\tJavascript")

favorite_language = 'Python '
print(len(favorite_language.rstrip()))
print(len(favorite_language))

#permanently strip space, assign to the variable
favorite_language =  favorite_language.rstrip()
print(len(favorite_language))
favorite_language = ' Python '
print(f"left strip : {favorite_language.lstrip()}")
print(f"right strip: {favorite_language.rstrip()}")
print(f"strip      : {favorite_language.strip()}")
print(favorite_language)
