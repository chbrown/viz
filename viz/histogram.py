from viz import terminal
from viz.text import format_float
import numpy as np


def hist(xs, range=None, margin=10, width=None):
    '''Usage:
    import scipy.stats
    draws = scipy.stats.norm.rvs(size=100, loc=100, scale=10)
    hist(draws, margin=5)
    '''
    # I'm not sure why my font in iterm doesn't like \u2588, but it looks weird.
    #   It's too short and not the right width.
    chars = u' \u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2589'
    # add 1 to each margin for the [ and ] brackets
    if width is None:
        width = terminal.width()

    bins = width - (2 * (margin + 1))
    # wrap it up as an array so we can index into it with a bool array. most likely it'll be a numpy array already
    xs = np.array(xs)
    finite = np.isfinite(xs)
    # don't copy it unless we need to (we don't need to if there are only finite numbers)
    # but if there are some nans / infinities, remove them
    finite_xs = xs[finite]  # if nonfinite.any() else xs
    # compute the histogram values as floats, which is easier, even though we renormalize anyway
    hist_values, bin_edges = np.histogram(finite_xs, bins=bins, density=True, range=range)
    # we want the highest hist_height to be 1.0
    hist_heights = hist_values / max(hist_values)
    # np.array(...).astype(int) will floor each value, if we wanted
    hist_chars = (hist_heights * (len(chars) - 1)).astype(int)
    cells = [chars[hist_char] for hist_char in hist_chars]

    print '%s[%s]%s' % (
        format_float(bin_edges[0], margin).rjust(margin),
        u''.join(cells),
        format_float(bin_edges[-1], margin).ljust(margin))
    if not finite.all():
        # if we took any out, report it:
        nonfinite_xs = xs[~finite]
        neginf = np.isneginf(nonfinite_xs)
        nan = np.isnan(nonfinite_xs)
        posinf = np.isposinf(nonfinite_xs)
        print '%s %s %s' % (
            ('(%d) -inf' % np.count_nonzero(neginf) if neginf.any() else '').rjust(margin),
            ('(%d) nan' % np.count_nonzero(nan) if nan.any() else '').center(len(cells)),
            ('(%d) +inf' % np.count_nonzero(posinf) if posinf.any() else '').ljust(margin)
        )
