"""
U2 Airline-Flottenerweiterung
"""

import xpress as xp

U2 = xp.problem()

# Variablen
x1 = xp.var() # Anzahl Kurzstreckenflugzeuge
x2 = xp.var() # Anzahl Mittelstreckenflugzeuge
x3 = xp.var() # Anzahl Langstreckenflugzeuge

U2.addVariable(x1, x2, x3)

# Nebenbedingungen
neb1 = 7*x1 + 10*x2 + 13.4*x3 <= 300 #Budget
neb2 =   x1 + x2 + x3 <= 30          #Besatzung
neb3 =   x1 + 4/3*x2 + 5/3*x3 <= 40  #Wartung

U2.addConstraint(neb1, neb2, neb3)

# Zielfunktion
objective = 0.46*x1 + 0.6*x2 + 0.84*x3

U2.setObjective(objective, sense=xp.maximize)

# Loesen und Ausgabe
U2.lpoptimize()

print("Lösung:", U2.getSolution())
print("ZFW:", U2.getObjVal())
print("Schattenpreise:", U2.getDual())
print("Schlupf:", U2.getSlack())
print("RCost:", U2.getRCost())

# Sensitivitätsanalyse für Zielfunktionskoeffizienten
lower_obj, upper_obj = [], []
U2.objsa([x1, x2, x3], lower_obj, upper_obj)
print("\nSensitivität für Zielfunktionskoeffizienten:")
print("Untere Grenzen:", lower_obj)
print("Obere Grenzen:", upper_obj)

# Sensitivitätsanalyse für Rechte Seiten (b-Vektor)
lower_rhs, upper_rhs = [], []
U2.rhssa([neb1, neb2, neb3], lower_rhs, upper_rhs)
print("\nSensitivität für Rechte Seiten:")
print("Untere Grenzen:", lower_rhs)
print("Obere Grenzen:", upper_rhs)