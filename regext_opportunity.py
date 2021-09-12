import re
import random


def captain_to_Mars():


    each_line = open('opportunity_log.txt').read().splitlines()
    quote_line =random.choice(each_line)
    print("regex_opp15",quote_line)

    mission_log = open('mission_log.txt').read().splitlines()
    mission_line =random.choice(mission_log)
    print("regex_opp16",mission_line)

    each_line = open('titles.txt').read().splitlines()
    title_line =random.choice(each_line)
    print("regex_opp17",title_line)
 
    return {'title': title_line,
            'quote': quote_line,
            'mission': mission_line}

     
