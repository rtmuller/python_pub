#Organize /downloads
import os

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
images_ext = ['.jpg', '.jpeg', '.png']
documents_ext = ['.txt', '.log', '.pdf']
torrents_ext = ['.torrent']
office_ext = ['.docx', '.xlsx', '.csv', '.doc', '.xls']
pem_ext = ['.pem']
zip_ext = ['.zip', '.rar']
sh_ext = ['.sh']


def get_extension(name):
    index = name.rfind('.')
    return name[index:]


def organizer(diretorio):
    AUDIOS_DIR =  os.path.join(diretorio, "audios")
    IMAGES_DIR =  os.path.join(diretorio, "images")
    DOCS_DIR =  os.path.join(diretorio, "documentos")
    VIDEOS_DIR =  os.path.join(diretorio, "videos")
    OTHERS_DIR =  os.path.join(diretorio, "others")
    TORRENTS_DIR = os.path.join(diretorio, "torrents")
    OFFICE_DIR = os.path.join(diretorio, "office")
    PEM_DIR = os.path.join(diretorio, "pem" )
    ZIP_DIR = os.path.join(diretorio, "zip")
    SH_DIR = os.path.join(diretorio, "sh")

    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OTHERS_DIR):
        os.mkdir(OTHERS_DIR)
    if not os.path.isdir(TORRENTS_DIR):
        os.mkdir(TORRENTS_DIR)
    if not os.path.isdir(OFFICE_DIR):
        os.mkdir(OFFICE_DIR)
    if not os.path.isdir(PEM_DIR):
        os.mkdir(PEM_DIR)
    if not os.path.isdir(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    if not os.path.isdir(SH_DIR):
        os.mkdir(SH_DIR)


    files_names = os.listdir(diretorio)
    new_directory = ''
    for file in files_names:
        if os.path.isfile(os.path.join(diretorio, file)):
            extension = str.lower(get_extension(file))
            print(file, extension)
            if extension in audios_ext:
                new_directory = AUDIOS_DIR
            elif extension in videos_ext:
                new_directory = VIDEOS_DIR
            elif extension in images_ext:
                new_directory = IMAGES_DIR
            elif extension in documents_ext:
                new_directory = DOCS_DIR
            elif extension in torrents_ext:
                new_directory = TORRENTS_DIR
            elif extension in office_ext:
                new_directory = OFFICE_DIR
            elif extension in pem_ext:
                new_directory = PEM_DIR
            elif extension in zip_ext:
                new_directory = ZIP_DIR
            elif extension in sh_ext:
                new_directory = SH_DIR
            else:
                new_directory = OTHERS_DIR
            old = os.path.join(diretorio, file)
            new = os.path.join(new_directory, file)
            os.rename(old, new)
            print("Moved:", old, "->", new)


if __name__ == '__main__':
    organizer('../../../downloads')