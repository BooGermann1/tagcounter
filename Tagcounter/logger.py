from datetime import datetime
from Tagcounter.misc import BadResultException


def log(filepath, url):
    date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    with open(filepath, 'a') as file:
        if not file.write('{0} {1}\n'.format(date, url)):
            """If file operation cannot be performed for some reason"""
            raise BadResultException('Operation cannot be logged')
