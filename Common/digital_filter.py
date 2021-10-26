import numpy as np
import scipy.signal


def filter_frequency_response(a, b, w=np.arange(0, np.pi, 0.1)):
    """
    Function that generates the frequency response of a digital filter given the coeficients of
    polynomials a0 + a_1*x + a_2*x^2 + ... and b0 + b_1*x + b_2*x^2 + ...
    This function evaluates the transfer function
    H(x)=(a0 + a_1*x + a_2*x^2 + ...)/(b0 + b_1*x + b_2*x^2 + ...) where x is an element in vector w.

    Parameters:
    w (numpy array): Array of natural frequency values.
    a (numpy array): Array of recursion coefficients a.
    b (numpy array): Array of recursion coefficients b.

    Returns:
    numpy array: Returns filter response.

    """
    z = np.exp(1j * w)

    a_degree = np.arange(0, len(a))
    b_degree = np.arange(0, len(b))

    N = len(z)
    na = len(a_degree)
    nb = len(b_degree)

    ZA = (np.repeat(z, na, axis=0)).reshape(N, na)
    ZB = (np.repeat(z, nb, axis=0)).reshape(N, nb)

    z_a = np.dot((ZA ** a_degree), a)
    z_b = np.dot((ZB ** b_degree), b)
    return z_a / z_b


def zeros_poles_gain(a, b):
    """
    Function that calculates the zeros, poles and gain of a given transfer function which consists of
    the coeficients of polynomials a0 + a_1*x + a_2*x^2 + ... and b0 + b_1*x + b_2*x^2 + ...

    Parameters:
    a (numpy array): Array of recursion coefficients a.
    b (numpy array): Array of recursion coefficients b.

    Returns: z,p,g
    z (numpy array): Zeros of transfer function.
    p (numpy array): Poles of transfer function.
    g (numpy array): Gain of transfer function.

    """
    return scipy.signal.tf2zpk(np.flip(a), np.flip(b))