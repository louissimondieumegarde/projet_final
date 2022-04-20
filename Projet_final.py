# Importer le package
import pandas

# Ouverture et lecture du fichier CSV
open("file.csv")
collisions_data = pandas.read_csv("file.csv", delimiter=",")

# Calcul des statistiques
# 1. Nombre d'accidents selon le jour de la semaine
print(collisions_data[["JR_SEMN_ACCDN", "NO_SEQ_COLL"]].groupby("JR_SEMN_ACCDN").count())

# 2. Nombre moyen de victimes par accident
nb_victimes_data = collisions_data["NB_VICTIMES_TOTAL"]
print(nb_victimes_data.mean())

# 3. Nombre d'accidents selon la condition meteorologique
print(collisions_data[["CD_COND_METEO", "NO_SEQ_COLL"]].groupby("CD_COND_METEO").count())

# 4. Nombre moyen de morts par accident
nb_morts_data = collisions_data["NB_MORTS"]
print(nb_morts_data.mean())

# 5. Nombre d'accidents selon le type d'eclairement
print(collisions_data[["CD_ECLRM", "NO_SEQ_COLL"]].groupby("CD_ECLRM").count())

# Creation d'un graphique avec les donnees
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV et transformer les dates du fichier en date reconnu par Python/Panda (parsing)
collisions = pandas.read_csv("file.csv", delimiter=",", parse_dates=["DT_ACCDN"])

# Regrouper les donnees des accidents par jour de la semaine
series_sales = collisions_data[["JR_SEMN_ACCDN", "NO_SEQ_COLL"]].groupby("JR_SEMN_ACCDN").count()

# Indiquer le type de diagramme
series_sales.plot(kind="bar")

# Afficher le diagramme
plt.show()
