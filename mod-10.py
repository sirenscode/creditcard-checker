def check_credit(card):
    card_list = [int(d) for d in card]
    checksum = card_list.pop()
    print(card_list)
    
    
    

    digits = list(reversed(card_list))
    digits.insert(0,0)
    for i in range(len(digits)):
        if i % 2 ==1:
            digits[i]*=2
            if digits[i] > 9:
                digits[i] = (int(str(digits[i])[0])+int(str(digits[i])[1]))
                
    total = sum(digits)+checksum
    print(total)
            
        
    if total % 10 == 0:
        print("VALID")
    else:
        print("INVALID")
            
    
    
            
        
    
    
check_credit("5154620020601637")
