import subprocess


class CheckSum:
    def __init__(self, exepath, rompath):
        self.exePath = exepath
        self.romPath = rompath

    def callsubprocess(self):
        subprocess.call([self.exePath, self.romPath])
