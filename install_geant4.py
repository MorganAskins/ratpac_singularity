import urllib.request
import os.path
from subprocess import call
import argparse

def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', action='store_true',
            help='Rebuild the base image')
    return parser.parse_args()

def download(url, name):
    print('Downloading %s to %s'%(url,name))
    if os.path.isfile(name) or os.path.isdir(name.split('.')[0]):
        print(' -- file already available, skipping')
        return
    urllib.request.urlretrieve(url, name)

def untar(tfile, odir):
    #cmd = 'tar -xzf %s --one-top-level=%s --strip-components=1' % (tfile, odir)
    cmd = 'tar -xzf %s -C %s --strip-components=1' % (tfile, odir)
    print(cmd)
    if os.path.isdir(odir):
        print(' -- dir already exists, skipping')
        return
    call(['mkdir',odir])
    call(cmd.split())

args = getargs()

files_to_download = { 
        'rootcern.tar.gz':'https://root.cern.ch/download/root_v5.34.32.source.tar.gz',
        'geant.tar.gz':'https://github.com/Geant4/geant4/archive/v10.4.2.tar.gz',
        'G4NEUTRONHPDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4NDL.4.5.tar.gz',
        'G4LEDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4EMLOW.7.3.tar.gz',
        'G4LEVELGAMMADATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.2.tar.gz',
        'G4RADIOACTIVEDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.2.tar.gz',
        'G4SAIDXSDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4SAIDDATA.1.1.tar.gz',
        'G4NEUTRONXSDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4NEUTRONXS.1.4.tar.gz',
        'G4ABLADATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4ABLA.3.1.tar.gz',
        'G4PIIDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz',
        'G4ENSDFSTATEDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.2.tar.gz',
        'G4REALSURFACEDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4RealSurface.2.1.1.tar.gz',
        'G4TENDLDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4TENDL.1.3.2.tar.gz',
        }

for k,v in files_to_download.items():
    download(v, k)

# Now we have the files, time to extract
dldir = []
for tarfile in files_to_download.keys():
    odir = tarfile.split('.')[0]
    dldir.append(odir)
    untar(tarfile, odir)

# Download the particular cmake needed for g4
download('https://cmake.org/files/v3.11/cmake-3.11.1-Linux-x86_64.sh', 'cmake.sh')

# Okay lets build Geant4

# Now build root?

# Cleanup
