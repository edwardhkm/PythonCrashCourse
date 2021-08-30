name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print(f"Hello, {name}!")

age = int(input("How old are you? "))
# print(type(age))
if age > 18:
    msg = "You are adult."
else:
    msg = "You are kid."
print(msg)


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello! {username.title()}!")


greet_user('jesse')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:  ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

