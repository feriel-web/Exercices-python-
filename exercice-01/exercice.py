

# 1. Déclarer les variables
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# 2. Calculer les totaux
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

# 3. Afficher le résultat avec une f-string
print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")

# 4. Convertir le prix texte en nombre
prix_texte = "19.90"
prix_ht = float(prix_texte)

# 5. Refaire le calcul
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")