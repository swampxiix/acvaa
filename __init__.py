import os
from z_constants import ACCTDIR

def contextInitialize(appServer, path):
    if not os.path.exists(ACCTDIR):
        os.mkdir(ACCTDIR)

