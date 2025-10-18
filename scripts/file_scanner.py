from api.logger import info
from api.utils import run_command

media_types = ('mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',
               'mp3', 'wav', 'flac', 'aac', 'ogg',
               'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')
executable_types = ('sh', 'bin', 'py', 'jar')
document_types = ('pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf')

all_types = media_types + executable_types + document_types

info("Scanning Files...")
def file_scanner():
    run_command(":")