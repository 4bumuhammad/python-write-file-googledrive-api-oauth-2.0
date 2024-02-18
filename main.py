from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

settings_path = './settings.yaml' 
gauth = GoogleAuth(settings_file=settings_path)
drive = GoogleDrive(gauth)

folder = "1wFXnCztdnawVpkNc_PWeUYVN97UQCqsI"

file1 = drive.CreateFile({'parents':[{'id': folder}], 'title': 'bismillah.txt'})
file1.SetContentString('Assalamualaikum Warahmatullah Wabarakatuh!')
# file1.SetContentFile()
file1.Upload()
