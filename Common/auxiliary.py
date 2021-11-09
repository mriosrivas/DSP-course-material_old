import numpy as np
from Common import fft
from Common import fourier_transform

def zero_padding(x, h):
    """ 
    Function that zero pads the smallest input signal.

    Attributes: 
    x(numpy array): Array of numbers representing an input signal.
    h(numpy array): Array of numbers representing an input signal.

    Returns: 
    x_pad(numpy array): Array of numbers representing an input signal x padded with zeros.
    h_pad(numpy array): Array of numbers representing an input signal h padded with zeros.
    """
    N = x.shape[0]
    M = h.shape[0]
        
    if(M<N):
        h_pad = np.append(h,np.zeros((N-M,1)), axis=0)
        x_pad = x
    elif(M>N):
        x_pad = np.append(x,np.zeros((N-M,1)), axis=0)
        h_pad = h
    else:
        x_pad = x
        h_pad = h
    
    return x_pad, h_pad
    
    
def zero_pad_fourier(x, M, method='FFT', L=1024):
    """
    Function to zero pad and calculate the Fourier Transform of a given signal. This function gives a "better
    resolution" when plotting our Fourier Transformations.
    :param x: (numpy array)  input signal to perform it's Fourier Transform.
    :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
            bandwidth of the transition band.
    :param method: (string) method to use for calculating the Fourier Transform, can be 'FFT'
            for Fast Fourier Transform or 'DFT' for Discrete Fourier Transform.
    :param L: (int) new size of signal x.
    :return: X: (numpy array) Fourier Transform of input signal x.
             f: (numpy array) normalized frequency between 0 and 0.5.
    """
    
    return None


def zero_pad(x, M, L=1024):
    """
    Function to zero pad a signal x to have a size of L.
    :param x: (numpy array)  input signal to perform pad with zeros.
    :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
            bandwidth of the transition band.
    :param L: (int) new size of signal x.
    :return: (numpy array) input signal padded with zeros. Number of padded zeros is L-M.
    """
    
    return None

