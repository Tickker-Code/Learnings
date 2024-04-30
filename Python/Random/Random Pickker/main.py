import random

def random_picker_num():
        thing = random.randrange(1,1000)
        return thing
        
def teller():
        number = random_picker_num()
        print(f'The number picked is...\n{number}\nCongratulations!')

teller()