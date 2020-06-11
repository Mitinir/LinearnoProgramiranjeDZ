# -*- coding: utf-8 -*-


"""
Freelance programer nudi dvije vrste usluga: konfiguriranje baze podataka i izrade web stranica 
te želi maksimizirati profit.
80€ po bazi, 100€ po stranici. Za bazu je potrebno 3 sata za projektiranje, a 2 sata za izradu,
a za stranicu treba 2 sata za projektiranje, a 3 za izradu.
Svakog tjedna programer ima 50 sati za projektiranje te 50 sati za programiranje.

x1 = broj izrađenih baza svaki tjedan
x2 = broj izrađenih stranica svaki tjedan

"""
from pulp import *

prob = LpProblem("Programer", LpMaximize)  # Stvaramo maksimizacijski LP problem
x1 = LpVariable("x1", lowBound=0) # Stvaramo varijablu x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Drugu varijablu x2 >= 0
prob += 80*x1 + 100*x2  # Objective funkcija, 80e za bazu, 100e za stranicu
prob += 3*x1 + 2*x2 <= 50, "Projektiranje hours, maksimalno 50"
prob += 2*x1 + 3*x2 <= 50, "Programiranje hours, maksimalno 50"
print("LP problem:", prob)  # Prikaz LP problema

status = prob.solve()  # Rijesi problem defaultnim solverom
print("Status rjesenja:", LpStatus[status])  # Ispisi status problema (optimalan?)
print("Vrijednost x1 = ", value(x1),"vrijednost x2 = ", value(x2), "max vrijednost objektivne funkcije = ", value(prob.objective))

"""
Recimo da prodajemo alkohol. Liker i vino. Pretpostavimo da nam za litru likera trebaju tri kile grožđa i dvije kile šećera.
Za vino nam trebaju 4 kg grožđa i 1 kg šećera.
Pretpostavimo da liker kupcu traje 25 dana, a vino 20 dana. Recimo i da imamo samo 25kg grožđa i 10kg šećera.
Koliko ćemo pića napraviti da kupcu traje što dulje?

x = likeri
y = vino
"""
# Stvaramo prob1 varijablu u kojoj su podaci o problemu
prob1 = LpProblem("Alkohol", LpMaximize)

# Stvaramo varijable
x = LpVariable("Liker_u_litrama",0,None,LpInteger)
y = LpVariable("Vino_u_litrama",0, None, LpInteger)

# Prvo objektivna funkcija
prob1 += 25*x + 20*y, "Kupljeno litara; to be maximized"
# Odredujemo uvjete
prob1 += 3*x + 4*y <= 25, "Grožđe constraint"
prob1 += 2*x + y <= 10, "Šećer constraint"
print("LP problem: ", prob1)
# The problem is solved using PuLP's choice of Solver
sol = prob1.solve()

print("Status rjesenja:", LpStatus[sol])  # Ispisi status problema (optimalan?)
print("Liker = ", value(x),"vino = ", value(y), "max litara napravljeno = ", value(prob1.objective))
