import random

def quote_of_day():
 
    each_line = open('riker_picard.txt').read().splitlines()
    quote_daily =random.choice(each_line)
    print(quote_daily)

    return quote_daily