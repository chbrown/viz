viz
===

Data visualization in the terminal.

Install
-------

**From PyPI:**

::

    easy_install viz

**From source:**

::

    git clone https://github.com/chbrown/viz.git
    cd viz
    python setup.py install

The main CLI script is ``viz``, which should be installed on your
``PATH``.

Examples
--------

Ping google every 100ms (0.1s) and plot the first 50 response times you
get back:

::

    ping -i 0.1 google.com | head -50 | sed -n 's/.*time=\(.*\) ms/\1/p' | viz hist

Example result (which should fit your terminal width automatically):

::

    26.1390000[ (cannot display with only ascii) ]39.5580000

Dependencies:
-------------

-  ``numpy``

License
-------

Copyright (c) 2013 Christopher Brown. `MIT
Licensed <https://raw.github.com/chbrown/viz/master/LICENSE>`__.
