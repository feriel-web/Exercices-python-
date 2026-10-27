
temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

# Moyenne arrondie à 2 décimales, minimum et maximum
moyenne = sum(temperatures) / len(temperatures)

print("Moyenne :", round(moyenne, 2), "°C")
print("Minimum :", min(temperatures), "°C")
print("Maximum :", max(temperatures), "°C")

# Compter les jours au-dessus de 15 °C
nb_jours = 0

for temperature in temperatures:
    if temperature > 15:
        nb_jours += 1

print("Jours au-dessus de 15 °C :", nb_jours)

# Convertir les températures en Fahrenheit
fahrenheit = [c * 9 / 5 + 32 for c in temperatures]

print("Températures en Fahrenheit :", fahrenheit)

# Afficher chaque jour avec enumerate
for i, temperature in enumerate(temperatures):
    print(f"Jour {i + 1} : {temperature} °C")
