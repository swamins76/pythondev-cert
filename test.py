import random
suit = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2,3,4,5,6,7,8,9,10]
lname = 'Shankar Subbu'
mylist = ["swami", "shankar", "subbu"]
#print (f'{fname.upper()} {lname}')
print ((mylist[2]))
def draw():
    which_suit = random.choice(suit)
    which_type = random.choice([faces, numbered])
    which_card = random.choice(which_type)
    return which_card; "of", which_suit


print (draw())
print(draw())
print(draw())