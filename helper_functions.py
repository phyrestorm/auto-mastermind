

def get_nth_place(n:int) -> str:

    switcher = {1: 'st',
                2: 'nd',
                3: 'rd'}

    unit = n % 10

    suffix = switcher.get(unit, 'th')
    str_place = str(n) + suffix

    return str_place