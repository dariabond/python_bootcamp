sentence = "What is the airspeed Velocity of an Unladen swallow"

words_list = sentence.split(" ")
print(words_list)
result = {word:len(word) for word in words_list}
print(result)
