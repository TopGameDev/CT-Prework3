def first_odds():
    x = 1
    while x <= 100:
        if x % 2 == 0:
            x += 1
            continue
        elif x % 2 == 1:
            numbers = x
            x += 1
            print(str(numbers) + " is odd! ")
    
first_odds()
