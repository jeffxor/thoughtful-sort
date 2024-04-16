
def is_bulky(width, height, length):
    volume = width * height * length
    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        return True
    else:
        return False
    
def is_heavy(mass):
    if mass >= 20:
        return True
    else:
        return False

def sort(width, height, length, mass):
    if is_bulky(width, height, length) and is_heavy(mass):
        return 'REJECTED'
    elif is_bulky(width, height, length) or is_heavy(mass):
        return 'SPECIAL'
    else:
        return 'STANDARD'


