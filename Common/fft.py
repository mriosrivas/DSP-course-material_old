import numpy as np


class FFT():
    def __init__(self):
        return 
    
    def fft(self, x, one_sided=True):
        """
        A vectorized, non-recursive version of the Cooley-Tukey FFT
        :param x: (numpy array) input signal.
        :param one_sided: (boolean) parameter to select between one sided spectrum if True or two sided
                spectrum if False.
        :return: (numpy array) one sided or two sided FFT of input signal x.
        """ 
        return None
        
    def ifft(self, x, one_sided=True):
        """
        A vectorized, non-recursive version of the Cooley-Tukey IFFT
        :param x: (numpy array) input signal.
        :param one_sided: (boolean) parameter to select between one sided spectrum reconstruction if True 
                or two sided spectrum reconstruction if False.
        :return: (numpy array) IFFT of input signal x.
        """
        return None

