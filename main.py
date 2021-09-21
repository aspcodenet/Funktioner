def introduction(first_name, last_name):
    print(f"Hello, my name is {first_name} {last_name}")


introduction("Stefan","Holmberg")

introduction(first_name = "James", last_name = "Bond")





def inputNamn(minLength, language = "sv"): 
    if language == "sv":
        print("Mata in namn:")
    else:
        print("Enter a name:")

    while True:
        namn = input()
        if len(namn) >= minLength:
            break
    return namn    


# a = "Mata in age"   
# x = int(input(a))
lang = input("Vilket språk vill du köra på")
# sv   en
forNamn = inputNamn(3)
efterNamn = inputNamn(6, "en")
merEfternamn = inputNamn(6, lang)


def HuvudMeny():
    a = 12345
    while True:
        print("*** HUVUDMENY *** ")
        print("1. Skapa")
        print("2. Login")
        print("3. Avsluta")
        sel = GetSelection(1,3)  
        if sel == 3:
            break
        if sel == 2:
            KontoMeny()

def KontoMeny():
    b = 1234
    print("*** KONTOMENY *** ")
    print("1. Ta ut")
    print("2. Saldo")
    print("3. Insätt")
    print("4. Back to huvudmeny")
    sel = GetSelection(1,4)
    if sel == 4:
        return


def GetSelection(min, max):
    while True:
        sel = int(input("Ange val:"))
        if sel >= min and sel <= max:
            return sel
        

HuvudMeny()

