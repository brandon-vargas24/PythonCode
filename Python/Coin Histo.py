from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

def coin_hist(n, p, k, cumulative=False):
    """Draw the histogram of the number of heads among n tosses of k coins.

    The probability of `heads` for each toss is p. If the cumulative flag is
    set to True, the histogram will be cumulative.
    """
    # n rows of k columns of coin tosses
    tosses = np.random.choice([1, 0], size=[n, k], p=[p, 1 - p])
    # sum along the rows: axis=0 means along columns, axis=1 means along rows.
    heads = tosses.sum(axis=1)
    print(heads)

    # "bins" for the histogram (bar chart). We get a column chart of the number
    # of elements in between each successive pair of bin markers.
    bins = np.arange(-0.5, k + 1.5)

    fig = plt.figure()
    # setting zorder to 3 brings the histogram to the front.
    plt.hist(heads, bins, color='g', cumulative=cumulative, zorder=3)
    plt.xlim(-1, k + 1)
    plt.title(('{:d} tosses of '.format(n) + '{:d} coins with '.format(k) +
               'success probability {:}'.format(p)))
    plt.xlabel('Number of heads')
    plt.ylabel('Number of occurrences')
    plt.grid(axis='both', zorder=1)  # push the grid lines to the back
    fig.savefig('Fig5.png')
    return None


coin_hist(10000, .2, 100, cumulative=False)
plt.show()
