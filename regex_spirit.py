import re



def twain_to_Mars():
 

    with open('spirit_log.txt') as mars:
        file = mars.read()

    # print (file)


    new = re.sub(r'Europe', 'Mars', file)
    # new += re.sub(r'Holy Land', 'space', file),
    # new += re.sub(r'Pleasure Excursion', 'rocket launch', file),
    # new += re.sub(r'America', 'world', file),
    # new += re.sub(r'Excursions', 'space exploration', file),
    # new += re.sub(r'picnic', 'space mission', file),
    # new += re.sub(r'participants', 'astronauts', file),
    # new += re.sub(r'steam ferry-boat', 'rocket ship', file),
    # new +=re.sub (r'creek', 'planet', file),
    # new += re.sub (r'grassy lawn', 'international space ship', file),
    # new +=re.sub (r'steamship', 'rocket shop', file)


    print (new)

    # mars.close()

    return new

