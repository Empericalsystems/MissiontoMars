import re



def twain_to_space():
 

    with open('curiosity_log.txt') as mars:
        file = mars.read()

    # print (file)


    new = re.sub(r'Marseilles', 'Mars', file)

    return new