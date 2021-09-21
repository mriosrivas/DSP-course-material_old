import numpy as np

class FourierTransform:
    def __init__(self, signal, correct_arctan=True, correct_unwrap=True, domain='fraction', **kwargs):
        """
        Function that calculates the DFT of an input signal.
        Parameters:
        signal(numpy array): Array of numbers representing the input signal to be transformed.
        correct_arctan (boolean): If True arctan correction is performed.
        correct_unwrap (boolean): If True phase abiguity correction is performed.
        
        Attributes: 
        signal (numpy array): Original input signal.
        N (int): Size of input signal.
        rex (numpy array): Real DFT part of input signal.
        imx (numpy array): Imaginary DFT part of input signal.
        magx (numpy array): Magnitude of the real and imaginary DFT.
        phasex (numpy array): Phase of the real and imaginary DFT.
        domain (numpy array): Frequency domain's independent variable.        
        """
        
        self.signal = None
        self.N = None
        self.rex, self.imx = None
        self.magx = None
        self.phasex = None
        self.domain = None
        return
        
        
    def dft(self, x):
        """ 
        Function that calculates the DFT of an input signal x.

        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be transformed.

        Returns: 
        rex (numpy array): Real DFT part of input signal x
        imx (numpy array): Imaginary DFT part of input signal x

        """

        
        return None, None  
    
    
    def dft_magnitude(self):
        """ 
        Function that calculates the magnitude of an real and imaginary signal x.

        Parameters: 
        rex (numpy array): Array of numbers representing the real part of the DFT signal.
        imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.

        Returns: 
        numpy array: Returns magnitude of the real and imaginary signal.

        """

        return None
    
    
    def dft_phase(self, correct_arctan=True, correct_unwrap=True):
        """ 
        Function that calculates the phase of an real and imaginary signal x. 
        Solving the different nuisances that might occur.

        Parameters: 
        rex (numpy array): Array of numbers representing the real part of the DFT signal.
        imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.
        correct_arctan (boolean): If True arctan correction is performed.
        correct_unwrap (boolean): If True phase abiguity correction is performed.

        Returns: 
        numpy array: Returns phase of the real and imaginary signal.

        """
        
        return None
    
    
    def arctan_correct(self, rex, imx, phase):
        """ 
        Function that corrects the arctan calculation. If both the real and 
        imaginary parts are negative, subtract 180 (or 𝜋 radians) from the
        calculated phase. If the real part is negative and the imaginary part
        is positive, add 180 (or 𝜋 radians)

        Parameters: 
        rex (numpy array): Array of numbers representing the real part of the DFT signal.
        imx (numpy array): Array of numbers representing the imaginary part of the DFT signal.
        phase (numpy array): Array of numbers representing the phase of the DFT signal.

        Returns: 
        numpy array: Returns corrected arctan calculation of phase.

        """

        
        return None
    
    
    def unwrap(self, phase):
        """ 
        Function that ensures that all appropriate multiples of 2𝜋 have been included.

        Parameters: 
        phase (numpy array): Array of numbers representing the phase of the DFT signal.

        Returns: 
        numpy array: Returns unwrapped phase.

        """

        
        return None
    
    
    def frequency_domain(self, style='fraction', **kwargs):
        """ 
        Function that calculates the frequency domain independent variable.

        Parameters: 
        obtain the frequency domain.
        style (string): String value that selects between frequency domain's 
        independent variable.
            'samples' returns number of samples between 0 to N/2
            'fraction' returns a fraction of the sampling rate between 0 to 0.5
            'natural' returns the natural frequency between 0 and pi.
            'analog' returns analog frequency between 0 and fsamp/2
        fsamp (float): Float value representing the sampling frequency. 
            (Only used for 'analog' style).

        Returns: 
        numpy array: Returns frequency domain's independent variable.

            """
        return None
