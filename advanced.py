#cards = input("Enter CC: ")

def check_credit(cards):
    cards_to_check = []
    for card_to_check in cards.splitlines():
        card_to_check = card_to_check.split("|")[0]
        cards_to_check.append(card_to_check)
        
    for card in cards_to_check:
        input_card = list(reversed([int(d) for d in card]))
        
        total = 0
        for i in range(len(input_card)):
            input_card[i]*=2
            if input_card[i] > 9:
                input_card[i] -= 9
                
        for i in range(len(input_card)):
            total += input_card[i]
            
        if total % 10 == 0:
            return "VALID"
        else:
            return "INVALID"
            
    
        
            
    #print(input_card)
        
        

cards = """
5514235014811301|06|2026|557
5514234373500258|05|2026|321
5514237725258384|02|2027|316
5514235514055540|10|2027|046
5514235285843223|07|2028|407
5514236646325025|11|2026|403
5514232203215287|04|2026|320
5514237836358123|07|2029|580
5514235221720436|03|2029|144
5514235630850568|02|2028|167
"""
if check_credit(cards):
    print("VALID")
else:
    print("INVALID")
    