import random

#print(random.randint(0,2))

NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]

failvar = 6
 

class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError("Неправильные параметры карты")

        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color


def create_cards():
    card1 = Card(NUMBERS[random.randint(0,2)], SYMBOLS[random.randint(0,2)], SHADINGS[random.randint(0,2)], COLORS[random.randint(0,2)])
    card2 = Card(NUMBERS[random.randint(0,2)], SYMBOLS[random.randint(0,2)], SHADINGS[random.randint(0,2)], COLORS[random.randint(0,2)])
    card3 = Card(NUMBERS[random.randint(0,2)], SYMBOLS[random.randint(0,2)], SHADINGS[random.randint(0,2)], COLORS[random.randint(0,2)])

    if not isinstance(card1, Card):
        return False
    if not isinstance(card2, Card):
        return False
    if not isinstance(card3, Card):
        return False

    cards = [card1, card2, card3]
    return cards

def check_set(cards):
    number = []
    symbol = []
    shading = []
    color = []
    for t in cards:
        number.append(t.number)
        symbol.append(t.symbol)
        shading.append(t.shading)
        color.append(t.color)


    preset = [number, symbol, shading, color]
    preset2 = []
    for ll in preset:
        for el in ll:
           preset2.append(el)
    SET = set(preset2)
    if len(SET) == 4:
        return True
    else:
        return False

#test = create_cards()
#print(test[0].number, test[1].number, test[2].number)
#print(test[0].symbol, test[1].symbol, test[2].symbol)
#print(test[0].shading, test[1].shading, test[2].shading)
#print(test[0].color, test[1].color, test[2].color)

#print(check_set(create_cards()))
#print(create_cards())
