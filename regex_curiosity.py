import re
import random

def twain_to_space():
 

    # with open('curiosity_log.txt') as mars:
    #     file = mars.read()
    each_line = open('curiosity_log.txt').read().splitlines()
    quote_line =random.choice(each_line)
    print(quote_line)
     

    mission_log = open('mission_log.txt').read().splitlines()
    mission_line =random.choice(mission_log)
    print(mission_line)
 
    return quote_line + mission_line
