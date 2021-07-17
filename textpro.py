input_str=[]
question=('how','when','what','why')

def sentence_maker(phrase):
    c=phrase.capitalize()
    if c.startswith(question):
        return"{}?".format(c)
    else:
        return"{}.".format(c)
while True:
    user_input = input('Say something:')
    if user_input=='\end':
       break
    else:
        input_str.append(sentence_maker(user_input))

print(" ".join(input_str))
