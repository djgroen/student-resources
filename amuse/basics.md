# Barebone pointers for AMUSE

The main code is available at http://www.amusecode.org. We have a working installation available on the Brunel Student machine.

## The full documentation for AMUSE can be found here:
http://www.amusecode.org/doc/

Numerous examples are provided here:
http://www.amusecode.org/doc/examples/

And tutorials are provided here:
http://www.amusecode.org/doc/tutorial/index.html


## Extra stuff required to install AMUSE from source at Brunel:

### Linux
Needs netcdf-dev and m4.

### Python
in $AMUSE_HOME/prerequisites/lib/python2.7/site-packages

``
cycler-0.10.0.dist-info       cython.pyc                    h5py                        mpi4py-1.3.1-py2.7.egg-info   numpy                       README
cycler.py                     dateutil                      h5py-2.3.1-py2.7.egg-info   netCDF4                       numpy-1.8.0-py2.7.egg-info  roman.py
cycler.pyc                    docutils                      matplotlib                  netCDF4-1.2.4-py2.7.egg-info  pyparsing-2.1.10.dist-info  roman.pyc
Cython                        docutils-0.7-py2.7.egg-info   matplotlib-2.0.0.egg-info   netcdftime                    pyparsing.py                six-1.10.0.dist-info
Cython-0.23.4-py2.7.egg-info  functools32                   matplotlib-2.0.0-nspkg.pth  nose                          pyparsing.pyc               six.py
cython.py                     functools32-3.2.3_2.egg-info  mpi4py                      nose-1.0.0-py2.7.egg-info     pyximport                   six.pyc
``

for sure the Python modules matplotlib, six, pyparsing, dateutil and functools32.

matplotlib also needs to be set up for grav_stellar.py, but for the time being that is recommended to be installed in a separate location, and its location to be appended to the $PYTHONPATH environment variable.


