"""
    This example shows multi-threading capabilities in Python
"""

import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('README.md', 'myarchive.zip')
background.start()  # invokes run() method in AsyncZip class
print('The main program continues to run in foreground.')

background.join()  # Puts main thread to pause and waits..
# ..for the background task to finish

print('Main program waited until background was done.')
