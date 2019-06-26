import time
import webbrowser

takeAwake = 0
print("take a break" + time.ctime())
while takeAwake < 3:
    # ! take break every 3 times for   30 minutes
    time.sleep(2)
    # ! the link for the song
    webbrowser.open("https://www.youtube.com/watch?v=Eb_TnPuC64k")
    #  ! incremting
    takeAwake += 1
