from mutagen.mp4 import MP4, MP4Cover, MP4Tags
from mutagen.mp3 import MP3

class Song(object):
    def __init__(self, filename):
        if filename.endswith('.m4a'):
            self.create_song_from_mp4(filename) 
        elif filename.endswith('.mp3'):
            self.create_song_from_mp3(filename)          
        else:
            print('"%s" is not a valid audio file.' % (file))

    def create_song_from_mp4(self, filename):
        audio = MP4(filename)
        print('"%s" by "%s" from %s.' % ( audio.tags['\xa9nam'][0], audio.tags['\xa9ART'][0], audio.tags['\xa9day'][0] ))

        covers = audio.tags['covr']

        if covers[0].imageformat == MP4Cover.FORMAT_JPEG:
            with open('cover.jpg', 'wb') as file:
                file.write(covers[0])
            print("Cover was written to file 'cover.jpg'.")
        else:
            print("Cover is a PNG.")
        
    def create_song_from_mp3(filename):
        audio = MP3(filename)
        for key in audio.tags:
            print(key)