import random


class Face:
    name=""
    def __str__(self):
        return self.name
    def __init__(self,name):
        self.name=name

class Dice:
    faces=[]

    def __init__(self, *faces):
        self.faces=faces

    def roll(self):
        return random.choice(self.faces)

class Deck:
    faces=[]
    extras=[]

    def append(self,face):
        self.faces.append(face)

    def extra(self,extra):
        self.extras.append(extra)

    def __str__(self):
        output=""
        for face in self.faces:
            output += str(face) + " "
        output += ": REAL=IDEAL\n\n"
        for extra in self.extras:
            output += str(extra) + "\n"

        return output

    def has_a(self,thing):
        for face in self.faces:
            if face.name==thing:
                return True
        return False

def is_complete(deck):
    return deck.has_a("A") and deck.has_a("S") and deck.has_a("Z")

quantordice = Dice(Face("forall"), Face("exists"), Face("forall"), Face("exists"), Face("exists"), Face("forall"))
partydice = Dice(Face("A"), Face("S"), Face("Z"))
eventdice = Dice(Face(""), Face(""), Face(""), Face(""), Face(""), Face("EVENT"))

deck = Deck()
events = ["Your notion is perfect!","The notion is statistical!","The simulator learns the environment's random coins!","The environment learns the simulator's random coins!","The environment is deterministic!","The simulator has white-box access to the adversary!","The simulator may rewind the adversary exactly once!"]

while not is_complete(deck):
    quantor = quantordice.roll()
    while quantor.name=="EVENT":
        if len(events)>0:
            random.shuffle(events)
            deck.extra(events.pop())
            quantor = quantordice.roll()
        else:
            quantor = quantordice.roll()

    party = partydice.roll()
    while str(party)=="EVENT":
        if len(events)>0:
            random.shuffle(events)
            deck.extra(events.pop())
            party = partydice.roll()
        else:
            party = partydice.roll()

    event = eventdice.roll()
    if str(event)=="EVENT":
        random.shuffle(events)
        deck.extra(events.pop())

    deck.append(quantor)
    deck.append(party)

print deck
