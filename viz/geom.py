import numpy as np

from . import terminal
from .stats import normalize
from .text import format_float


def hist(xs, range=None, margin=10, width=None):
    """
    xs: array of numbers, preferably an np.array, can contain nans, infinities
    range: (minimum, maximum) tuple of numbers (defaults to (min, max) of xs)
    margin: number of characters to use for the min-max labels (default: 10)
    width: number of characters that will fit in a row (defaults to your terminal width)

    Example:

    >>> import scipy.stats
    >>> draws = scipy.stats.norm.rvs(size=100, loc=100, scale=10)
    >>> hist(draws, margin=5)
    """
    if width is None:
        width = terminal.width()

    # add 1 to each margin for the [ and ] brackets
    n_bins = width - (2 * (margin + 1))
    # wrap it up as an array so we can index into it with a bool array. most likely it'll be a numpy array already
    xs = np.array(xs)
    finite = np.isfinite(xs)
    # don't copy it unless we need to (we don't need to if there are only finite numbers)
    # but if there are some nans / infinities, remove them
    finite_xs = xs[finite]  # if nonfinite.any() else xs
    # compute the histogram values as floats, which is easier, even though we renormalize anyway
    values, bin_edges = np.histogram(finite_xs, bins=n_bins, density=True, range=range)
    # we want the highest height to be 1.0
    heights = values / max(values)
    # np.array(...).astype(int) will floor each value, if we wanted
    hist_chars = (heights * (len(terminal.bars) - 1)).astype(int)
    cells = [terminal.bars[hist_char] for hist_char in hist_chars]

    print(
        format_float(bin_edges[0], margin).rjust(margin),
        "[" + "".join(cells) + "]",
        format_float(bin_edges[-1], margin).ljust(margin),
        sep="",
    )
    if not finite.all():
        # if we took any out, report it:
        nonfinite_xs = xs[~finite]
        preds = [np.isneginf, np.isnan, np.isposinf]
        # names = ["-inf", "nan", "+inf"]
        names = [
            pred.__name__[len("is") :].replace("pos", "+").replace("neg", "-")
            for pred in preds
        ]
        counts = [np.count_nonzero(pred(nonfinite_xs)) for pred in preds]
        col1, col2, col3 = [
            f"({count:d}) {name}" if count else "" for count, name in zip(counts, names)
        ]
        print(col1.rjust(margin), col2.center(len(cells)), col3.ljust(margin))


def points(ys, width=None):
    """
    Usage:
    import scipy.stats
    def walk(steps, position=0):
        for step in steps:
            position += step
            yield position
    positions = list(walk(scipy.stats.norm.rvs(size=1000)))
    points(positions)
    """
    if width is None:
        width = terminal.width()

    ys = np.array(ys)
    n = len(ys)
    y_min, y_max = np.min(ys), np.max(ys)
    n_bins = min(width, n)
    bins_per_n = float(n_bins) / float(n)
    # print n, n_bins, n_per_bin, bins_per_n
    sums = np.zeros(n_bins)
    counts = np.zeros(n_bins)
    for i, y in enumerate(ys):
        bin = int(i * bins_per_n)
        sums[bin] += y
        counts[bin] += 1
    bin_means = sums / counts
    # we want the lowest bin_height to be 0.0, and highest bin_height to be 1.0
    bin_heights = normalize(bin_means)
    bin_chars = (bin_heights * (len(terminal.bars) - 1)).astype(int)
    # print sums, counts, bin_means
    cells = [terminal.bars[bin_char] for bin_char in bin_chars]
    print("[%+f]" % y_max)
    print("".join(cells))
    print("[%+f]" % y_min)
