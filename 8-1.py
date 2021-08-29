# 8-1
def display_message():
    print(f"I am learning python.")


display_message()


# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("Alice in Wonderland")

# 8-3, 8-4
def make_shirt(msg_to_print='I love Python', size='large'):
    print(f"The t-shirt size is {size}, message to print is {msg_to_print}")


make_shirt(1, "LALALA")
make_shirt(size=2, msg_to_print="kkk")
make_shirt(size='medium')
make_shirt()
make_shirt(size='small', msg_to_print='uuu')

# 8-5
def describe_city(name, country='Australia'):
    print(f"{name} is in {country}")

describe_city('Sydney')
describe_city('HK', 'HK')
describe_city('Tokyo', 'Japan')
