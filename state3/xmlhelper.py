class MyXMLHelper(object):
    def __init__(self,filePath):
        self.filePath = filePath

    def to_utf_8str(self):
        try:
            f = open(self.filePath, "r")
            r = f.read()
            text = str(r.encode('utf-8'), encoding = "utf-8")
            return text
        finally:
            if f:
                f.close()
        
    