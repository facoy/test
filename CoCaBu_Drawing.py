#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # plt.plot([1, 2, 3, 4])
    # plt.ylabel('some numbers')
    # plt.show()
    #
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    # plt.axis([0, 6, 0, 20])
    # plt.show()

    t = np.arange(0., 100., 0.2)

    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()
