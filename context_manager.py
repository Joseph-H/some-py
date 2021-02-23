import sqlite3
from urllib.request import urlopen
from contextlib import closing, contextmanager, supress, redirect_stdout

# context manager allows you to "open" something, use it and then it gets closed. For example:
"""
with open(path, 'w') as f_obj:
    f_obj.write(some_data)
"""

# create a context manager that connects to a database
class DataConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    # this method gets executed automatically because of the with statement
    def __enter__(self):
        """
        Open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    # once everything is done and the program goes outside the scope of the with
    # exit gets called
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'test.db'
    with DataConn(db) as conn:
        cursor = conn.cursor()


# context manager with contextmanager decorator - this is handy and let's you skip enter and exit
# as lines from the filed are available, they are yielded. If an error happens or the file is done then finally is called
# you can say this is self closing

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()

if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')

# there is a function you can use that will let you create a context manager and close it for you when the code
# goes out of scope
with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass


# another handy function is supress, if you want to supress errors do this
with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

# redirect std out
path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        # by using the help method here the output is getting written to the file
        help(redirect_stdout)
