#Questo è un commento di prova
def LoadTweets():
    #Questo è una funzione di prova
    pass

inserimento = input("Inserisci del testo\n")

print(inserimento)


def Confronto(Primo,Secondo):
    if (Primo > Secondo):
        return 1
    elif (Primo == Secondo):
        return 0
    elif (Primo < Secondo):
        return -1


a = Confronto(10,21)
b = Confronto(1,1)
c = Confronto(90,1)

print("Primo valore",a,"Secondo Valore",b,"Terzo Valore",c)


def NRigheVuote(n):
    while (n != 0):
        print("",".")
        n = n - 1

NRigheVuote(10)
