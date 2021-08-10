import numpy as np
import matplotlib.pyplot as plt


class Plot:

    def __init__(self):
        pass

    def plot_multiple(self, signal):
        """
        Function that plots a impulse/step decomposition of a signal.
        :param signal: (numpy array) square matrix of impulse/step decomposition where each row 
        represents a single impulse/step decomposition of each n-th sample.
        :return: None
        """

        plt.rcParams["figure.figsize"] = (15, 25)

        delta = 1
        y_min = signal.min() - delta
        y_max = signal.max() + delta

        N = signal.shape[0]

        if N % 2 != 0:
            M = N + 1
        else:
            M = N

        for i in range(M):
            plt.subplot(int(M / 2), 2, i + 1)
            try:
                plt.stem(signal[i], use_line_collection=True);
                plt.ylim((y_min, y_max))
                plt.title("Sample: {}".format(i))
                plt.grid()
            finally:
                pass
        return

    def plot_single(self, signal, title="Signal", style='stem'):
        """
        Function that plots stem of a given signal.
        :param signal: (numpy array) array of numbers to be plotted.
        :param title: (string) title to be used, by default "Signal" is used.
        :param style: (string)
        :return: None
        """
        delta = 1

        plt.rcParams["figure.figsize"] = (10, 5)

        if style == 'stem':
            plt.stem(signal[0], use_line_collection=True)
        elif style == 'line':
            plt.plot(signal[0])

        try:
            y_min = signal.min() - delta
            y_max = signal.max() + delta
            plt.ylim((y_min, y_max))
        except:
            pass

        plt.title(title)
        plt.grid()
        return
    
    def plot_three_signals(self, x1, x2, x3, titles=('x1', 'x2', 'x3'), labels=('sample', 'sample', 'sample')):
        """
        Funtion that allows to plot three signals at the same time.
        :param x1: (numpy array) signal 1
        :param x2: (numpy array) signal 2
        :param x3: (numpy array) signal 3
        :param titles: (tuple) titles for each signal, by default titles are set to ('x1', 'x2', 'x3').
        :param labels: (tuple) labels for each signal, by default labels are set to ('sample', 'sample', 'sample').
        :return: None
        """

        plt.rcParams["figure.figsize"] = (25, 10)
        plt.subplot(2, 2, 1)
        plt.plot(x1)
        plt.title(titles[0])
        plt.xlabel(labels[0])

        plt.subplot(2, 2, 2)
        plt.plot(x2)
        plt.title(titles[1])
        plt.xlabel(labels[1])

        plt.subplot(2, 1, 2)
        plt.plot(x3)
        plt.title(titles[2])
        plt.xlabel(labels[2])

        plt.tight_layout(pad=3.0)

        plt.show()
        return

    def plot_frequency_response(self, x, f, title="Frequency Response of Filter", label=None):
        """
        Function to plot power frequency response of a given filter. Power of a signal x is calculated as
        follows P=20*log(x).
        :param x: (numpy array) input filter.
        :param f: (numpy array) normalized frequency between 0 and 0.5.
        :param title: (string) string of title to use.
        :param label: (string) string of label to use.
        :return: None
        """
        # We use this to avoid discontinuities in our plot
        x[0][0] = x[1][0]
        x[-1][0] = x[-2][0]

        x_log = 20 * np.log10(x)
        plt.plot(f, x_log, label=label)
        plt.title(title)
        plt.xlabel("Normalized frequency")
        plt.ylabel("Gain [dB]")
        plt.grid("on")
        return

    def plot_zeros_poles(self, z, p):
        """
        Function that plots zeros and poles of transfer function

        Parameters:
        z (numpy array): Array of zeros.
        p (numpy array): Array of poles.

        Returns:
        Plot of zeros and poles of transfer function.

        """
        ax = plt.subplot(133)
        x = np.arange(-1, 1, 0.00001)
        y = np.zeros(len(x))
        ax.plot(x, np.sqrt(1 - x ** 2), 'black')
        ax.plot(x, -np.sqrt(1 - x ** 2), 'black')
        ax.plot(np.real(z), np.imag(z), 'bo', fillstyle='none', markersize=12)
        ax.plot(np.real(p), np.imag(p), 'rx', markersize=12)
        ax.grid(b=True, which='major')
        axis_x = np.arange(-1.5, 1.5, 0.00001)
        axis_y = np.zeros(len(axis_x))
        ax.plot(axis_x, axis_y, 'gray')
        ax.plot(axis_y, axis_x, 'gray')
        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        plt.xlabel('Re')
        plt.ylabel('Im')
        return

