# This is my dictionary 3 languages with 3 integers
language = {'java': 5, 'c++': 4, 'html': 3, 'css': 2}
# Loops through the dictionary
# Prints the key and value
for k , v in language.items():
    print(k, v)

# Dictionary will have the topic, definition, hint
protocol = {'application': 'http', 'transport': 'tcp', 'internet': 'ip', 'link': 'Ethernet'}
for l, p in protocol.items():
    print("Layer is " + l + " layer protocol is: " + p)