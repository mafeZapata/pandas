from git import Repo

# Ruta al repositorio de Git
ruta_repositorio = 'C:\Users\DELL\Documents\enfasis\git\pandas'

# Ruta al archivo en el repositorio
ruta_archivo = 'pandas/_config/config.py'

# Inicializar el objeto Repo
repo = Repo(ruta_repositorio)

# Obtener el historial de commits del archivo
commits = list(repo.iter_commits(paths=ruta_archivo))

# Recorrer los commits y obtener los detalles
for commit in commits:
    print("Commit:", commit.hexsha)
    print("Autor:", commit.author.name)
    print("Fecha:", commit.authored_datetime)
    print("Mensaje:", commit.message)
    print("---")
