import os
import os.path
from os import path
import random
from picture import HentaiPicture
from statusnaked import StatusNaked

ALLOWED_FILETYPES = [
    ".png",
    ".tif",
    ".tiff",
    ".jpg",
    ".jpeg"
]

def main():
    print("starting: just some good hentai manager")
    if not path.exists("Porn"):
        os.mkdir("Porn")
        print("Folder created")
        return
    else:
        print("Folder already exists")
        for filename in os.listdir("Porn"):
            file_extension = os.path.splitext(filename)
            if file_extension[1] in ALLOWED_FILETYPES:
                print("Das File wird unterstützt:", filename)
                buildfile(filename)
            else:
                print("Das file wird nich unterstützt:", filename)

def buildfile(file):
    HentaiPicture(
        random.randint(100000, 999999),
        bool(input("Zensiert oder Unzensiert?")),
        StatusNaked[input("Wie nackt")],
        bool(input("Ist es Bdsm?")),
        int(input("Wie viele Leute sind auf dem Bild?")),
        bool(input("Ist es Anime oder Real Porn?")),
        [],
        bool(input("Bekannte oder Unbekannte Person")),
        str(input("Von welchem Artist ist das Bild"))
    )

if __name__ == "__main__":
    main()

"""
Bild
    rndm id
    Zensatur status
    wie viel haut wird gezeigt
    bdsm hardcore shit
    personen anzahl
    real oder anime
    parent(s)
    person:
        known
        unknown
    artist    
"""