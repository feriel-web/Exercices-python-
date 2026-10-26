# Partie 1 : Classer les températures

temperatures = [-3, 0, 15, 31]

for temperature in temperatures:
    if temperature < 0:
        categorie = "gel"
    elif temperature < 15:
        categorie = "froid"
    elif temperature < 25:
        categorie = "doux"
    else:
        categorie = "chaud"

    print(f"{temperature} °C : {categorie}")


# Partie 2 : Vérifier si une année est bissextile

annees = [2024, 1900, 2000]

for annee in annees:
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")
