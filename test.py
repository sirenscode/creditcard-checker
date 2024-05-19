card = "5514236646325025|11|2026|403"
cards = """5154620020606305|02|2029|635
5154620020601512|11|2032|486
5154620020607170|09|2032|808
5154620020601637|11|2025|238
5154620020602254|06|2028|013
5154620020605737|03|2025|250
5154620020601736|04|2026|562
5154620020605273|01|2024|961
5154620020607824|11|2031|864
5154620020603476|07|2031|496
"""

def check_credit(card):
    card = card.split("|")[0]
    input_card = list(reversed([int(d) for d in card]))
    
    for i in range(len(input_card)):
        input_card[i]*=2
        if input_card[i] > 9:
            input_card[i] -= 9
    
    total = 0
    for i in range(len(input_card)):
        total += input_card[i]
        
    if total % 10 == 0:
        return True
    else:
        return False
    
print("\n\nCREDIT CARD CHECKER V1.0\n\n")
for card in cards.splitlines():
    if check_credit(card):
        print(f'[✅] {card.replace("|", " | ")}')
    else:
        print(f'[❌] {card.replace("|", " | ")}')

print("\n\nFollow me on telegram: https://t.me/toxic_sirens\n\n")

