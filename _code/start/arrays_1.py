#Sorter array/liste fra lavest til høyest
def sorter(tall):
    return sorted(tall)


#Sorter fra høyest til lavest
def sorter_rev(tall):
    return sorted(tall)[::-1]


#Eksempelliste med tallene 1-6
liste = [2, 6, 4, 3, 5, 1]

#Skriv ut liste
print(liste)

#Skriv ut sortert liste
print(sorter(liste))

#Skriv ut liste som er sortert fra høyest til lavest
print(sorter_rev(liste))