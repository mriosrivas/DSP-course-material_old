import numpy as np
import matplotlib.pyplot as plt


class FIR():
    def __init__(self):
        return
        
    def shifted_sinc(self, fc, M):
        """
        Function that performs the calculation of a sinc shifted function.
        :param fc: (float) cut-off frequency for the low-pass filter. Between 0 and 0.5.
        :param M: (int) length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :return: (numpy array) sinc shifted time domain response.
        """     
        return None
        
    
    def hamming_window(self, M):
        """
        Function that calculates a Hamming window of a given M-kernel.
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :return: (numpy array) Hamming window of a given M-kernel.
        """
            
        return None
    
    
    def blackman_window(self, M):
        """
        Function that calculates a Blackman window of a given M-kernel.
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :return: (numpy array) Blackman window of a given M-kernel.
        """
        return None
        
    
    def window_filter(self, fc, M, normalized=True, window_type='hamming'):
        """
        Function to calculate the window filter based on the product of an window and a sinc function.
        :param fc: (float) cut-off frequency of a low pass filter
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :param normalized: (boolean) parameter to set normalized output, by default is set to True.
        :param window_type: (string) window to use, can be 'hamming' for Hamming window or 'blackman' for
                Blackman window. By default 'hamming' is used.
        :return: (numpy array) filter of sinc and window functions of a given M-kernel.
        """
        return None
       
    
    def spectral_reversal(self, x):
        """
        Function that implements the spectral reversal algorithm.
        :param x: (numpy array) filter of sinc and window functions of a given M-kernel to be spectral reversed.
        :return: (numpy array) filter of a spectral reversed sinc and window functions of a given M-kernel.
        """
        
        return None
    
    def spectral_inversion(self, x):
        """
        Function that implements the spectral inversion algorithm.
        :param x: (numpy array) filter of sinc and window functions of a given M-kernel to be spectral inverted.
        :return: (numpy array) filter of a spectral inverted sinc and window functions of a given M-kernel.
        """      
        return None
        
    
    def low_pass_filter(self, fc, M, window_type='blackman', normalized=True):
        """
        Function that calculates a low pass FIR filter.
        :param fc: (float) cut-off frequency for the low pass filter.
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :param window_type: (string) window to use, can be 'hamming' for Hamming window or 'blackman' for
                Blackman window. By default 'hamming' is used.
        :param normalized: (boolean) parameter to set normalized output, by default is set to True.
        :return: (numpy array) coefficients of a low pass FIR filter of size M.
        """
        return None
        
    
    def high_pass_filter(self, fc, M, method='spectral_inversion', window_type='blackman', normalized=True):
        """
        Function that calculates a high pass FIR filter.
        :param fc: (float) cut-off frequency for the high pass filter.
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :param method: (string) parameter that selects between the 'spectral_inversion' and
                'spectral_reversal' methods, by default 'spectral_inversion' is used.
        :param window_type: (string) window to use, can be 'hamming' for Hamming window or 'blackman' for
                Blackman window. By default 'hamming' is used.
        :param normalized: (boolean) parameter to set normalized output, by default is set to True.
        :return: (numpy array) coefficients of a high pass FIR filter of size M.
        """
        return None
        
    
    def band_filter(self, fc1, fc2, M, band_type='pass', method='spectral_inversion',
                    window_type='hamming', normalized=True):
        """
        Function that calculates a band/reject pass FIR filter.
        :param fc1: (float) cut-off frequency for the filter.
        :param fc2: (float) cut-off frequency for the filter.
        :param M: (int) Length of the filter kernel. Usually M = 4/BW, where BW is the filter
                bandwidth of the transition band.
        :param band_type: (string) type of filter, if 'pass' a pass band filter is constructed, if 'reject'
                a reject band filter is constructed.
        :param method: (string) parameter that selects between the 'spectral_inversion' and
                'spectral_reversal' methods, by default 'spectral_inversion' is used.
        :param window_type: (string) window to use, can be 'hamming' for Hamming window or 'blackman' for
                Blackman window. By default 'hamming' is used.
        :param normalized: (boolean) parameter to set normalized output, by default is set to True.
        :return: (numpy array) coefficients of a band pass (if method='pass') or a reject band
                (if method='reject') FIR filter of size M.
        """
        
        return None
