import subprocess
import os


def kolla_version(version):
    with open("release.txt", "w") as fil:
        fil.read(version)


def kör_git_kommando(kommando):
    try:
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"


läsa_fil = kolla_version()
merge = kör_git_kommando("git merge origin main")
