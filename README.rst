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

The CLI entry point is ``viz``, which should be installed on your
``PATH``.

Commands
--------

``viz hist``
~~~~~~~~~~~~

Read floats from ``stdin`` and plot as a single line histogram.

**Example**: ping google every 100ms (0.1s) and plot the first 50
response times you get back:

::

    ping -i 0.1 google.com | head -50 | sed -n 's/.*time=\(.*\) ms/\1/p' | viz hist

Example result (which should fit your terminal width automatically):

::

    26.1390000[▁      ▁▁  ▁▁▂▂ ▉ ▂▂ ▃ ▂▁▂ ▁ ▁▁      ▁   ▁                                    ]39.5580000

``viz total``
~~~~~~~~~~~~~

Read floats from ``stdin`` and sum them. No graphics, but useful because
``awk '{sum+=$1}END{print sum}`` is too long.

**Example**: count the bytes used by the current directory and its
children.

::

    find . -ls | tr -s ' ' | cut -d ' ' -f 7 | viz total

Example result:

::

    8519086.0

Compare to du:

::

    echo $[$(du -sk . | cut -f 1) * 1024]
    > 8531968

``viz points``
~~~~~~~~~~~~~~

Read floats from ``stdin``, plot on a single line from left to right
with as much granularity as the terminal will allow. Otherwise, bin
incrementally and plot the arithmetic mean of each bin.

**Example**: ping some really awful website every 100ms, plot the first
100 successful responses (takes about 10s).

::

    ping -i 0.1 godaddy.com | head -100 | sed -n 's/.*time=\(.*\) ms/\1/p' | viz points

Example result:

::

    [+156.298000]
       ▃▃ ▁▃          ▁ ▁▁ ▁    ▁  ▁▁▁▂ ▃▂ ▉▂              ▁ ▁▁      ▁▂▁       ▁  ▁          ▁      ▁
    [+70.593000]

The top line is the maximum, the bottom is the minimum. The other values
are scaled linearly between those extremes.

Dependencies:
-------------

-  ``numpy``

Related projects (mostly graphical visualizations for Python)
-------------------------------------------------------------

-  `Matplotlib <http://matplotlib.org/api/pyplot_api.html>`__: feels
   archaic to the touch. The pyplot fans have never run ``import this``,
   the interface is unguessable and murkily documented.
-  `Bokeh <http://bokeh.pydata.org/quickstart.html>`__: haven't used yet
-  `Vispy <http://vispy.org/>`__: haven't used yet

License
-------

Copyright (c) 2013 Christopher Brown. `MIT
Licensed <https://raw.github.com/chbrown/viz/master/LICENSE>`__.
