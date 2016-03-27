from mutagen.mp4 import MP4, MP4Cover, MP4Tags
from mutagen.mp3 import MP3
import os

def read_mp4(file):
    audio = MP4(file)
    print('"%s" by "%s" from %s.' % (audio.tags['\xa9nam'][0], audio.tags['\xa9ART'][0], audio.tags['\xa9day'][0], ))

    covers = audio.tags['covr']

    if covers[0].imageformat == MP4Cover.FORMAT_JPEG:
        with open('cover.jpg', 'wb') as file:
            file.write(covers[0])
        print("Cover was written to file 'cover.jpg'.")
    else:
        print("Cover is a PNG.")
        
def read_mp3(file):
    audio = MP3(file)
    for key in audio.tags:
        print(key)

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.m4a'):
            read_mp4(os.path.join(subdir, file)) 
        elif file.endswith('.mp3'):
            read_mp3(os.path.join(subdir, file))          
        #else:
        #    print('"%s" is not a valid audio file.' % (file))