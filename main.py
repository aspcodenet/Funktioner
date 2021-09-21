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
    print("*** HUVUDMENY *** ")
    print("1. Skapa")
    print("2. Login")
    print("3. Avsluta")

def KontoMeny():
    print("*** KONTOMENY *** ")
    print("1. Ta ut")
    print("2. Saldo")
    print("3. Insätt")
    print("4. Avsluta")


def GetSelection(min, max):
    while True:
        sel = int(input("Ange val:"))
        if sel >= min and sel <= max:
            return sel
        

while True:
    HuvudMeny()
    sel = GetSelection(1,3)  
    #if .... 
    KontoMeny()  
    sel = GetSelection(1,4)

