import random

def lista_segreta(max_range):
    lista = []
    colori = []
    icol= ["blu","grigio","verde","rosso","nero","rosa","giallo","viola","marrone","bianco"]
    for i in range(4):
        colori.append(icol[random.randint(1, len(icol))])
    return colori


lista_mastermind=lista_segreta(5)
print(lista_mastermind)


corrette =0
tentativi =0
flag1=0
flag2=0
flag3=0
flag4=0
print("############BENVENUTO AL GIOCO DI MASTERMIND!!!!!!!!!#####################\n")
print("############PROVA A INDOVINARE I NUMERI SEGRETI #####################\n")
while corrette < 4:

    if flag1==False:
        col1=str(input("Indovina il primo colore: \n"))
        if col1 == lista_mastermind[0]:
            corrette += 1
            print("Corretto!")
            flag1 = True
        elif col1 in lista_mastermind:
                print("Colore corretto ma posizione sbagliata")
        else:
            print("sbagliato!")
            flag1=False

    elif flag2==False:
        col2=str(input("Indovina il secondo colore: \n"))
        if col2 == lista_mastermind[1]:
            corrette += 1
            print("Corretto!")
            flag2 = True


        elif col2 in lista_mastermind:
            print("Colore corretto ma posizione sbagliata")
        else:
            print("sbagliato!")
            flag2 = False
    elif flag3==False:
        col3=str(input("Indovina il terzo colore: \n"))
        if col3 == lista_mastermind[2]:
            corrette += 1
            print("Corretto!")
            flag3 = True


        elif col3 in lista_mastermind:
            print("Colore corretto ma posizione sbagliata")
        else:
            print("sbagliato!")
            flag3 = False
    elif flag4 == False:

        col4=str(input("Indovina il quarto colore: \n"))
        tentativi=+1
        if col4 == lista_mastermind[3]:
            corrette +=1
            print("Corretto!")
            flag4 = True

        elif col4 in lista_mastermind:
            print("Colore corretto ma posizione sbagliata")
        else:
            print("sbagliato!")
            flag4 = False

        if corrette <  4:
            print("Hai indovinato "+ str(corrette)+" numeri correttamente")
            corrette=0
            continue
        else:
            print ("Bravo, hai indovinato tutti i quattro numeri, ci hai messo "+str(tentativi)+" tentativi")
