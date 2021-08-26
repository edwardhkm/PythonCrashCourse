transports = ['bus', 'car', 'bicycle']

message = f"I would like to own a {transports[0]}."
message = f"I would like to own a {transports[1]}."
message = f"I would like to own a {transports[2]} and a {transports[0]}."
print(message)
message2 = "{} {} are good".format(transports[0], transports[1])
print(message2)