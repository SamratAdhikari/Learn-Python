# Automatic Folder Cleaner

# modules
import os

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")



if __name__ == '__main__':
    path = str(input("Enter the path of files: "))
    os.chdir(path)
    files = os.listdir()
    # print(files)
    # folder = input("Enter the name of Folder: ")
    create("Images")
    create("Media")
    create("Docs")
    create("Other")

    imgExt = [".png", ".ico", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
    # print(images)

    docExt = [".txt", ".docx", ".pdf", ".doc", ".accdb", ".pptx", ".pub", ".rar", ".zip", ".spv"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
    # print(docs)

    mediaExt = [".mp3", ".mp4", ".mkv", ".ts", ".flv"]
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
    # print(media)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExt) and (ext not in imgExt) and (ext not in docExt) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", media)
    move("Other", others)

