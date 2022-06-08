def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'