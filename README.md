# numpy-exemple
Définir les données expérimentales avec numpy
Ce code permet de réaliser une régression linéaire simple à partir d'un jeu de données expérimentales x et y. La droite de régression est tracée en rouge sur un graphique représentant les données expérimentales sous forme de points verts.
Le code utilise la fonction linregress de la bibliothèque scipy.stats pour calculer la pente et l'ordonnée à l'origine de la droite de régression, ainsi que le coefficient de corrélation entre x et y.
Le graphique est créé avec la fonction subplots de la bibliothèque matplotlib.pyplot, puis les points expérimentaux sont tracés avec la fonction scatter et la droite de régression est tracée avec la fonction plot. Les axes et la légende du graphique sont définis avec les fonctions set_xlabel, set_ylabel, set_title et legend.
Enfin, les valeurs de la pente, de l'ordonnée à l'origine et du coefficient de corrélation sont affichées avec la fonction print.
