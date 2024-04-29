import re
import sys
from text_generation_server.cli import app

if __name__ == '__main__':

    args = 'serve google/gemma-2b-it --port 8080'
    # args = 'serve --help'

    sys.argv = sys.argv[:1] + args.split()
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(app())









