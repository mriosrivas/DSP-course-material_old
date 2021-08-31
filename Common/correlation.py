import numpy as np
from Common import convolution


class Correlation():
    
    def __init__(self):
        self.convolve = convolution.Convolve()
        pass
    
    
    def correlation(self, x, h, algorithm='output'):
        """ 
        Function that finds the correlation of an input signal x with an step response h.
        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be correlated.
        h (numpy array): Array of numbers representing the unit step response of a filter or signal.
        algorithm (string): String that selects the algoritm to use for finding the convolution.
                            Can be `fast` if `conv1d` function is used, `input` if `convolve_input_algorithm`
                            is used, and `output` if `convolve_output_algorithm` is used. Default value is
                            `output`.

        Returns: 
        numpy array: Returns correlation r_xh[n]=x[n]*h[-n].

        """
        
            
        return None
    
    
    def auto_corr(self, x, algorithm='output'):
        """ 
        Function that finds the auto correlation of an input signal x.
        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be auto correlated.
        algorithm (string): String that selects the algoritm to use for finding the convolution.
                            Can be `fast` if `conv1d` function is used, `input` if `convolve_input_algorithm`
                            is used, and `output` if `convolve_output_algorithm` is used. Default value is
                            `output`.

        Returns: 
        numpy array: Returns auto correlation r_xx[n]=x[n]*x[-n].

        """
        
        return None
    
    
    def norm_correlation(self, x, h, algorithm='output'):
        """ 
        Function that finds the normalized correlation of an input signal x with an step response h.
        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be correlated.
        h (numpy array): Array of numbers representing the unit step response of a filter or signal.
        algorithm (string): String that selects the algoritm to use for finding the convolution.
                            Can be `fast` if `conv1d` function is used, `input` if `convolve_input_algorithm`
                            is used, and `output` if `convolve_output_algorithm` is used. Default value is
                            `output`.

        Returns: 
        numpy array: Returns normalized correlation y[n]=r_xh[n]/(sqrt(max(r_xx[n])*max(r_hh[n]))).

        """
        
        return None
    
    
    def norm_auto_corr(self, x, algorithm='output'):
        """ 
        Function that finds the normalized auto correlation of an input signal x.
        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be auto correlated.
        algorithm (string): String that selects the algoritm to use for finding the convolution.
                            Can be `fast` if `conv1d` function is used, `input` if `convolve_input_algorithm`
                            is used, and `output` if `convolve_output_algorithm` is used. Default value is
                            `output`.

        Returns: 
        numpy array: Returns normalized auto correlation y[n]=r_xx[n]/max(r_xx[n]).


        """
        
        return None

    
    def delay(self):
        """ 
        Function that finds the lag between a signal x[n] with respect to the filter or signal h[n].
        Before invoking this function, self.correlation() must be invoked.
        Parameters: 
        None

        Returns: 
        numpy value: Returns negative difference between maximum correlation index and (filter lenght - 1).


        """
        return None
        
