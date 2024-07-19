Creating Intensity Graphs with `lampy`
======================================

The :class:`~lampy.BalmerLines` class has multiple methods for plotting intensity graphs
with the help of matplotlib.

    >>> import lampy

    >>> # Creating an instance of the class
    >>> length = 100
    >>> maxdist = 2 * u.kpc
    >>> ncells = 100
    >>> dl = 46 * u.pc
    >>> l = 6 * u.deg
    >>> b = 5 * u.deg

    >>> synthetic_line = BalmerLines(length, dl, l=l, b=b, dustmap_class = BayestarQuery)

The code above will create an instance of the class. You can decide which graphs you would like
by doing the following codes:

    >>> # Plot H-alpha Intensity with dust correction for multiple cells at a range of velocities
    >>> synth.plot_intensity('ha', extinction_correction=True)
    >>>
    >>> # Plot H-alpha Intensity without dust correction for multiple cells at a range of velocities
    >>> synth.plot_intensity('ha', extinction_correction=False)
    
