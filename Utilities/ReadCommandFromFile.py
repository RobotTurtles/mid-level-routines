import os
import errno

class ReadCommandFromFile(object):

    def __init__(self, cmdFile):
        self.cmdFile = cmdFile
        pass

    def get_command(self):

        self.open_commands()

        cmd = ''

        with open(self.cmdFile, 'r') as cmdFile:
            cmd = cmdFile.readline().strip()

        return cmd

    def open_commands(self):
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        try:
            file_handle = os.open(self.cmdFile, flags)
        except OSError as e:
            if e.errno == errno.EEXIST:  # Failed as the file already exists.
                pass
            else:  # Something unexpected went wrong so reraise the exception.
                raise

    def clear_commands(self):
        os.remove(self.cmdFile)


