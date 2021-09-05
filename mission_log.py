import random

def mars_missionblog():
 

    # with open('curiosity_log.txt') as mars:
    #     file = mars.read()
    each_line = open('Mission_log.txt').read().splitlines()
    quote_line =random.choice(each_line)
    print(quote_line)