f = lambda x: x % 2 == 0  # die Funktion muss einen Wahrheitswert zurückgeben

liste = [4, 2, 5, 6, 3]
list2 = list(filter(f, liste))

print(list2)
