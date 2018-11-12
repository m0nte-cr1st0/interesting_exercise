import random


def number_to_fortune(number):
    """Сhoose a random answer."""
    if number == 0:
        return 'Yes, for sure!'
    if number == 1:
        return 'Probably yes.'
    if number == 2:
        return 'Seems like yes...'
    if number == 3:
        return 'Definitely not!'
    if number == 4:
        return 'Probably not.'
    if number == 5:
        return 'I really doubt it...'
    if number == 6:
        return 'Not sure, check back later!'
    if number == 7:
        return "I really can't tell"
    else:
        return 'Error'

def mystical_octosphere(question):
    """Form the answer."""
    print('Your question was... ' + question)
    print('You shake the mystical octosphere.')
    
    answer_number = random.randrange(0, 7, 1)
    answer_fortune = number_to_fortune(answer_number)

    print("The cloudy liquid swirls, and a reply comes into view...")
    print("The mystical octosphere says... " + answer_fortune)
    print() 
    
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
