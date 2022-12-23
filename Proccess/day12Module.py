import string

def random_user_id():
    keyw = string.ascii_letters+string.digits+string.ascii_letters+string.ascii_letters+string.digits+string.digits
    return keyw

print(random_user_id())