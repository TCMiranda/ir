import os
import dropbox
from dropbox import files

OPERATIONS_FILEPATH = 'export_operacoes.txt'

def download_dropbox_file():
    dbx = dropbox.Dropbox(os.environ['DROPBOX_API_KEY'])
    # Do not raise if the file is initially empty
    try:
        dbx.files_download_to_file(OPERATIONS_FILEPATH, os.environ['DROPBOX_FILE_LOCATION'])
    except dropbox.exceptions.ApiError:
        pass
    except:
        raise

    try:
        dbx._session.close()
    except:
        pass


def upload_dropbox_file(file_from, file_to):
    dbx = dropbox.Dropbox(os.environ['DROPBOX_API_KEY'])
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=files.WriteMode.overwrite)
    try:
        dbx._session.close()
    except:
        pass
