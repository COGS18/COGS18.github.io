"""Copy files from notebooks/ to assets/downloads and zip."""

import os
import os.path as op
from zipfile import ZipFile

##
##

path_root = op.join(op.dirname(op.abspath(__file__)), '..')

nb_path = op.join(path_root, 'notebooks')
dl_path = op.join(path_root, 'assets', 'downloads')

notebooks = [ff for ff in os.listdir(nb_path) if '.ipynb' in ff]

for notebook in notebooks:
    ZipFile(op.join(dl_path, notebook + '.zip'), mode='w').write(op.join(nb_path, notebook), notebook)

print('Notebooks copied for download.')
