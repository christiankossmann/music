import os
import sys
import song

# check if filename is provided as command line argument
if len(sys.argv) != 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(2)
    
filename = sys.argv[1]
song = song.Song(filename)

#for subdir, dirs, files in os.walk(os.getcwd()):
#    for file in files:
#        if file.endswith('.m4a'):
#            read_mp4(os.path.join(subdir, file)) 
#        elif file.endswith('.mp3'):
#            read_mp3(os.path.join(subdir, file))          
        #else:
        #    print('"%s" is not a valid audio file.' % (file))