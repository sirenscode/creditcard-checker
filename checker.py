def check_credit(card_no):
    no_of_digits = len(card_no)
    sum = 0
    isSecond = False
    
    for i in range(no_of_digits - 1, -1, -1):
        input_no = (ord(card_no[i]) - ord('0'))
        
        if(isSecond == True):
            input_no = input_no * 2
            
        sum += input_no // 10
        sum += input_no % 10
        
        isSecond = not isSecond
        
    if (sum % 10 ==0):
        return True
    else:
        return False
        
        
        

if(check_credit("79927398713")):
    print("VALID")
else:
    print("INVALID")