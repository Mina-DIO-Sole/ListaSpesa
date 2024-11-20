#Creare un programma per gestire una lista della spesa. Il
#programma deve permettere di aggiungere, visualizzare e
#rimuovere elementi dalla lista.

#1
lista_vuota = []


#2
def aggiungi():
    elemento = input("Inserisci l'elemento da aggiungere alla lista: ")
    lista_vuota.append(elemento)
    print(f'"{elemento}" braavoo ricky aggiunto.')


#3
def visualizza():
 for i in range(len(lista_vuota)):
  print(f"{i + 1}. {lista_vuota[i]}")

#4
def  rimuovi_elemento_easy():
lista_vuota.remove("mela")


def contaElementi():



def svuota_lista():
   


def menu():
    while True:
        print("\nMenu:")
        print("1. Aggiungi un elemento alla lista")
        print("2. Visualizza la lista")
        print("3. Rimuovi un elemento dalla lista ")
        print("4. conta elemetni lista ")
        print("5. Esci")

        scelta = input("Seleziona un'opzione (1-4): ")

        if scelta == "1":
            aggiungi()
        elif scelta == "2":
            visualizza()
        elif scelta == "3":
            rimuovi_elemento_easy()
        elif scelta  == "4":
           contaElementi()
        elif scelta == "5":
            print("bravo esci")
            break
        elif scelta == "6":
            svuota_lista()
        else:
            print("Scelta no Riprova.")