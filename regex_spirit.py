import re
import random


def troi_to_Mars():
 
    each_line = open('spirit_log.txt').read().splitlines()
    quote_line =random.choice(each_line)
    print(quote_line)

    mission_log = open('mission_log.txt').read().splitlines()
    mission_line =random.choice(mission_log)
    print(mission_line)
 
    return quote_line + mission_line


    

