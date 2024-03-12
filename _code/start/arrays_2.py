# Lager en eksempel liste med tilfeldige tall mellom 0 og 10
import random
def random_liste(str, lav, hoy):
    #Lager en tom liste
    liste = []

    #Tell fra 0 til tallet i str og gjør dette frem til tallet er nådd
    for i in range(str):
        #Lag et tilfeldig tall
        tall = random.randint(lav, hoy)

        #Legg til det tilfeldige tallet i listen (som siste element)
        liste.append(tall)
    
    #Send en ferdig utfylt liste med tilfeldige tall tilbake
    return liste

#Lag en tilfeldig liste og lagre den som "tilfeldig_liste"
tilfeldig_liste = random_liste(10, 0, 10)

#Skriv ut "tilfeldig_liste" som en liste
print(tilfeldig_liste)

#For hvert tall som finnes i "tilfeldig_liste"
for tall in tilfeldig_liste:
    #Skriv det ut
    print(tall)