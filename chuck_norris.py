from chucknorris.pronoun import nick_gender


def chuck(name):
    return name + " is a " + nick_gender(name)


print(chuck("Marcel"))