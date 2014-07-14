Installing CERN's ROOT software framework
=========================================

CERN#s ROOT web page already has an
[installation guide](http://root.cern.ch/drupal/content/installing-root-source)
for installing ROOT from the source code, but for convenience here's a brief
guide.

## Xubuntu 13.04 (64-bit)

First, create a directory for installing ROOT. For example, you
may wish to put ROOT in a `software` directory in your home folder:

    cd ~              # Go to your home folder.
    mkdir software    # A folder for software, if you don't have one already.
    cd software

Then get ROOT from CERN's git repository. We'll be using version 5.34.

    git clone http://root.cern.ch/git/root.git root-v5-34
    cd root-v5-34
    git checkout -b v5-34-08 v5-34-08

Then install the "prequisite software", as described on the ROOT
installation guide
[here](http://root.cern.ch/drupal/content/build-prerequisites)
(you will need to enter your Linux account password when prompted):

    sudo apt-get install git dpkg-dev make g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev gfortran libssl-dev libpcre3-dev xlibmesa-glu-dev libglew1.5-dev libftgl-dev libmysqlclient-dev libfftw3-dev cfitsio-dev graphviz-dev libavahi-compat-libdnssd-dev libldap2-dev python-dev libxml2-dev libkrb5-dev libgsl0-dev libqt4-dev

Then run the ROOT configuration script. This prepares your system for the
install, as well as specifiying which bits of ROOT you want to use.
Again, copying and pasting this should be fine:

    ./configure --enable-fftw3 --enable-gviz --enable-gdml --enable-genvector --enable-mathmore --enable-minuit2 --enable-mysql --enable-opengl --enable-python --enable-qt --enable-roofit --enable-xml --enable-x11

This should finish telling you that everything is fine, and you're ready to
build the software by typing:

    make -j3

**Warning: this will take some time**. Make a cup of tea or something.

Once that's finished, you should be able to do the following:


    source ~/software/root-v5-34/bin/thisroot.sh # Runs the setup script.
    root                                         # Starts ROOT.

This ROOT title picture should appear - congratulations, you've installed ROOT!
