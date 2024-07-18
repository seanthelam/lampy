Installing ``whampy``
=====================

Requirements
------------

This package has the following dependencies:

* `Python <http://www.python.org>`_ 3.10 or later
* `Numpy <http://www.numpy.org>`_ 1.26 or later
* `Astropy <http://www.astropy.org>`_ 5.3 or later
* `matplotlib <http://matplotlib.org>`_ 3.8 or later
* `pandas <http://pandas.pydata.org>`_ 2.2 or later
* `seaborn <http://seaborn.pydata.org>/index.html>`_ 0.12 or later

Installation
------------

You can install lampy using pip::

  pip install lampy

To stall the latest developer version of lampy you can type::

    git clone https://github.com/seanthelam/lampy.git
    cd lampy
    python setup.py install

You may need to add the ``--user`` option to the last line `if you do not
have root access <https://docs.python.org/2/install/#alternate-installation-the-user-scheme>`_.
You can also install the latest developer version in a single line with pip::

    pip install git+https://github.com/seanthelam/lampy.git
