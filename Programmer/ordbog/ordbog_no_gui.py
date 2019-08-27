import pickle

filename = "pickleordbog"
ordbog = {
}
infile = open(filename, "rb")
ordbog = pickle.load(infile)
infile.close()


def indtast():
    outfile = open(filename, "wb")
    dkord = input("Indtast dansk ord:")
    ukord = input("Indtast engelsk ord:")
    ordbog[dkord] = ukord
    pickle.dump(ordbog, outfile)
    outfile.close()
    menu()


def søg():
    input("Søg på ord: ")


def udskriv():
    for key, value in ordbog.items():
        print(key+": "+value)
    menu()


def menu():
    valg = input("Indtast dit valg: ")
    if valg == "søg":
        søg()
    elif valg == "tilføj ord":
        indtast()
    elif valg == "vis ordbog":
        print(ordbog)
    elif valg == "afslut":
        exit()
    else:
        print("Fejl")


menu()
