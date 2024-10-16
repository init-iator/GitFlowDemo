import subprocess
import os


def kör_git_kommando(kommando):
    try:
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"


def öppna_versions_fil():
    with open("release.txt", "r") as fil:
        version = fil.read()
        return version


def spara_versions_fil(currentVersion):
    currentVersion = currentVersion.split(".")  # ["1", "0", "0"]
    newVersion = int(currentVersion[0]) + 1
    with open("release.txt", "w") as fil:
        fil.write(newVersion)


version = öppna_versions_fil()
print(f"Nuvarande version: {version}")

print(f"Kör 'branch release-{version}':")
output = kör_git_kommando(f"git branch release-{version}")
print(output)

output = kör_git_kommando(f"git push origin release-{version}")
print(output)

spara_versions_fil()
