import numpy as np
from scipy.linalg import toeplitz

class Convolve:
    
    def __init__(self):
        pass
    
    
    def conv1d(self, x, h):
        """ 
        Function that convolves an input signal x with an step response h using a Toeplitz matrix implementation.

        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be convolved.
        h (numpy array): Array of numbers representing the unit step response of a filter.

        Returns: 
        numpy array: Returns convolved signal y[n]=h[n]*x[n].

        """
        
        return None


    def convolve_output_algorithm(self, x, h):
        """ 
        Function that convolves an input signal x with an step response h using the output side algorithm.

        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be convolved.
        h (numpy array): Array of numbers representing the unit step response of a filter.

        Returns: 
        numpy array: Returns convolved signal y[n]=h[n]*x[n].

        """
        
        return None
    
    
    
    def convolve_input_algorithm(self, x, h):
        """ 
        Function that convolves an input signal x with an step response h using the input side algorithm.
      
        Parameters: 
        x (numpy array): Array of numbers representing the input signal to be convolved.
        h (numpy array): Array of numbers representing the unit step response of a filter.
      
        Returns: 
        numpy array: Returns convolved signal y[n]=h[n]*x[n].
      
        """
        
    
        return None
        
        
    def conv2d(self, image, kernel):
        """ 
        Function that convolves an input image with a filter kernel.
      
        Parameters: 
        image (numpy matrix): Matrix representing a 2D image.
        kernel (numpy array): An m by n matrix to apply.
      
        Returns: 
        numpy matrix: Returns convolved image with filter kernel.
      
        """
       
        return None
        
        
    def first_difference(self, x):
        """ 
            Function that calculates the first difference of an input signal x using the recursive
            equation y[n]=x[n]-x[n-1].

            Parameters: 
            x (numpy array): Array of numbers representing the input signal.

            Returns: 
            numpy array: Returns first difference of input signal x.

            """

        
        return None
    
    
    def running_sum(self, x):
        """ 
            Function that calculates the running sum of an input signal x using the recursive
            equation y[n]=x[n]+y[n-1].

            Parameters: 
            x (numpy array): Array of numbers representing the input signal.

            Returns: 
            numpy array: Returns running sum of input signal x.

            """
       
        return None
