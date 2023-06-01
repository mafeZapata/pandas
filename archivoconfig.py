import sys
from git import Repo

# Ruta al repositorio de Git
ruta_repositorio = 'C:\\Users\\DELL\\Documents\\enfasis\\git\\pandas'

# Ruta al archivo en el repositorio
ruta_archivo = 'pandas/core/arrays/datetimelike.py'

# Inicializar el objeto Repo
repo = Repo(ruta_repositorio)

# Obtener el historial de commits del archivo
commits = list(repo.iter_commits(paths=ruta_archivo))

# Establecer la codificación de la salida estándar
sys.stdout.reconfigure(encoding='utf-8')

# Recorrer los commits y obtener los detalles
for commit in commits:
    print("Commit:", commit.hexsha)
    print("Autor:", commit.author.name)
    print("Fecha:", commit.authored_datetime)
    print("Mensaje:", commit.message)
    print("---")

