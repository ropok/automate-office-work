import os
import shutil

class moveDir():
    # set directory
    def __init__(self, dir):
        super(moveDir, self)
        self.dir = dir
        self.date = ""
        self.path = os.path.join(self.dir, self.date)
	
def moveDir(src, dst):
	shutil.move(src, dst)

