import wikipedia





def get_wiki(msg):
    return wikipedia.summary(msg,sentences=3)

