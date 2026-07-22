from pathlib import Path
from urllib.request import urlretrieve
import subprocess
import os

def automatic_choose (useronly, list):
    if useronly:
        if os.environ['HOME']+"/.local/bin" in list :
            return(os.environ['HOME']+"/.local/bin")
        else:
            return("E")
    else:
        if "/bin" in list:
            return("/bin")
        elif "/usr/bin" in list:
            return("/usr/bin")
        elif "/usr/local/bin" in list:
            return("/usr/local/bin")
        else:
            return("E")

pathstr= os.environ['PATH']
path_list=pathstr.split(":")
print('''Choose for who to install:
1.Install for all user (need to have administrator privilege)
2.Install just for my user''')
choise=input('>')

if choise == "1":
    forallpath = []
    for path in path_list:
        if not os.environ['HOME'] in path:
            forallpath.append(path)
    print("Choose the path for instalation")
    autopath=automatic_choose(False,forallpath)
    if autopath=="E":
        i=0
    else:
        print("1.Choose automatically("+autopath+")")
        i=1
    for path in forallpath:
        i+=1
        print(str(i)+"."+path)
    pathindextoinstall=input(">")
    if pathindextoinstall=="1" and autopath!="E":
        installpath=autopath
    else:
        if autopath=="E":
            installpath=useronlypath[int(pathindextoinstall)+1]
        else:
            installpath=useronlypath[int(pathindextoinstall)+2]

if choise == "2":
    useronlypath=[]
    for path in path_list:
        if os.environ['HOME'] in path:
            useronlypath.append(path)
    print("Choose the path for instalation")
    autopath=automatic_choose(True,useronlypath)
    if autopath=="E":
        i=0
    else:
        print("1.Choose automatically("+autopath+")")
        i=1
    for path in useronlypath:
        i+=1
        print(str(i)+"."+path)
    pathindextoinstall=input(">")
    if pathindextoinstall=="1" and autopath!="E":
        installpath=autopath
    else:
        if autopath=="E":
            installpath=useronlypath[int(pathindextoinstall)+1]
        else:
            installpath=useronlypath[int(pathindextoinstall)+2]

print("Do you want to install in this location:",installpath,"(Y/N)")
yn=input(">")
if yn =="Y":
    urlretrieve("https://github.com/nepusoft/sony_playingback_to_gif/raw/refs/heads/main/main.py", "main.py")
    os.rename("main.py",installpath+"/main.py")

    sh = open(installpath+"/playingback2gif.sh", "x")
    sh.write("python3 main.py")
    sh.close()
    Path(installpath+"/playingback2gif.sh").chmod(0o755)


#command = ["sh",""]
#pathprocess = subprocess.run(command, capture_output=True, text=True)
#path = pathprocess.stdout()