import os
import sys

# Récupérer les commits via arguments si besoin
badhash = sys.argv[1]  # mauvais commit
goodhash = sys.argv[2]  # bon commit

# Démarrer le bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter bisect avec les tests
# Ici, python manage.py test retourne 0 si OK, non-zero sinon
os.system("git bisect run python manage.py test")

# Après avoir trouvé le commit fautif, réinitialiser bisect
os.system("git bisect reset")
