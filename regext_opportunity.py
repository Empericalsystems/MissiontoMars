import re



def opportunity_to_Mars():
 

    with open('opportunity_log.txt') as mars:
        file = mars.read()

    # print (file)


    new = re.sub(r'Europe', 'Mars', file)

    ee = re.sub(r'Holy Land', 'space', file)
    # abc = re.sub(r'Pleasure Excursion', 'rocket launch', file)

    # new += re.sub(r'Excursions', 'space exploration', file),
    # new += re.sub(r'picnic', 'space mission', file),
    # new += re.sub(r'participants', 'astronauts', file),
    # new += re.sub(r'steam ferry-boat', 'rocket ship', file),
    # new +=re.sub (r'creek', 'planet', file),
    # new += re.sub (r'grassy lawn', 'international space ship', file),
    # new +=re.sub (r'steamship', 'rocket shop', file)


    print (new)

    # mars.close()

    return new, ee