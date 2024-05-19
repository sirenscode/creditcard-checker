import sys

checksum = 0
def check_credit(card):
    card = [int(d) for d in card.replace("	","")]
    if card != []:
        global checksum
        checksum = card.pop()
    card = list(reversed(card))
    
    card.insert(0,0)
    
    for i in range(len(card)):
        if i % 2 == 1:
            card[i] *= 2
            if card[i] > 9:
                card[i] -= 9
            
    
    total = sum(card)+checksum
    
    if total % 10 == 0:
        return True
    else:
        return False
    
cards = """
6011046695915352
6011011662884023
6011965315133242277
"""
    
for card in cards.splitlines():
    if check_credit(card):
        print("VALID")
    else:
        print("INVALID")