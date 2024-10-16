import subprocess
import os
# subprocess.run(["ls", "-l"])
# if not (os.path.exists("Diverse")):
#     subprocess.run(
#         ["git", "clone", "https://github.com/init-iator/Diverse.git"])
# # os.chdir("C:\chasAcademy\Systemutveckling-Python\pythonGit\Diverse")
# newFolder = os.path.join(os.getcwd(), "Diverse")
# # print(newFolder)
# # subprocess.call("ls", shell=True, cwd=newFolder)
# # subprocess.run(["git", "checkout", "-b", "testbranch"], cwd=newFolder)
# # subprocess.run(["git", "checkout", "-b", "testbranch"])
# subprocess.run(["git", "push", "-u", "origin", "testbranch"], cwd=newFolder,)


def kör_git_kommando(kommando):
    try:
        # Kör git-kommandot med subprocess
        resultat = subprocess.run(kommando)
        return resultat.stdout
    except Exception as error:
        return f"Ett fel uppstod: {error}"


print("Kör 'git status':")
output = kör_git_kommando("git status")


print(output)
