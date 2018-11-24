import random

print("CIAO a tutti " + str(random.random()))

selezione = input("Give me a number : ")
try:
    if int(selezione) > 10:
        print("Valid number %d" % int(selezione))
    else:
        print("Little number %d" & int(selezione))
except ValueError as err:
    print("ERROR : " + str(err))

