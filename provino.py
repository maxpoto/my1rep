print("CIAO a tutti")
selezione = input("Give me a number : ")
try:
    if int(selezione) > 10:
        print("Valid number")
    else:
        print("Little number")
except ValueError as err:
    print("ERROR : " + str(err))

