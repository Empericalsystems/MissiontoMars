import re
import random

def spock_to_space():
 

    # with open('curiosity_log.txt') as mars:
    #     file = mars.read()
    each_line = open('curiosity_log.txt').read().splitlines()
    quote_line =random.choice(each_line)
    print("regex_cur9", quote_line)
     

    mission_log = open('mission_log.txt').read().splitlines()
    mission_line =random.choice(mission_log)
    print("regex_cur10",mission_line)
 
    each_line = open('titles.txt').read().splitlines()
    title_line =random.choice(each_line)
    print("regex_cur11",title_line)
 
    return {'title': title_line,
            'quote': quote_line,
            'mission': mission_line}
