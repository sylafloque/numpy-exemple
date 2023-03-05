import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Définition des données expérimentales
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 3.7, 4.8, 6.2, 7.5])

# Modélisation d'une régression linéaire
pente, ordonnee_origine, correlation, p_value, erreur_standard = linregress(x, y)

# Calcul des valeurs prédites de y pour chaque x
y_pred = pente * x + ordonnee_origine

# Tracé du graphique
fig, ax = plt.subplots()
ax.scatter(x, y, color='green', label='Données expérimentales')

# Tracé de la droite de régression
droite_reg = f'Régression linéaire : y={pente:.2f}x+{ordonnee_origine:.2f}'
ax.plot(x, y_pred, color='red', label=droite_reg)

# Légende et axes du graphique
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Modèle de régression linéaire')

# Affichage du graphique
plt.show()

# Affichage de la pente, de l'ordonnée à l'origine et du coefficient de corrélation
print(f'Pente : {pente:.2f}')
print(f'Ordonnée à l\'origine : {ordonnee_origine:.2f}')
print(f'Coefficient de corrélation : {correlation:.2f}')
