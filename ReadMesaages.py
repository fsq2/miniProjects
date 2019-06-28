import urllib.request


def ReadText():
    re = open('C:\\Users\\sfw20\\Desktop\\movie.txt')
    outpot = re.read()
    CheckForBadWord(outpot)


def CheckForBadWord(text):
    check_text = urllib.parse.quote(text)
    print(check_text)

    connections = urllib.request.Request(
        "http://www.wdylike.appspot.com/?q="+check_text)

    response = urllib.request.urlopen(connections)
    output = str(response.read())
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("The document has no bad words.")
    else:
        print("Unable to scan the document.")


ReadText()
