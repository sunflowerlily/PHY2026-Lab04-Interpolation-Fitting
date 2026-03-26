import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def breit_wigner(E, f_r, E_r, Gamma):
    return f_r / ((E - E_r)**2 + Gamma**2 / 4)

def weighted_fit():
    E_data = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200], dtype=float)
    g_data = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7], dtype=float)
    err = np.array([9.34, 17.9, 41.5, 85.5, 51.5, 21.5, 10.8, 6.29, 4.14], dtype=float)
    
    initial_guess = [100000, 75, 50]
    
    popt_unweighted, _ = curve_fit(breit_wigner, E_data, g_data, p0=initial_guess)
    
    # TODO 1: 在 curve_fit 中加入 sigma 与 absolute_sigma=True 完成加权拟合
    popt_weighted, pcov_weighted = None, None
    
    if popt_weighted is not None:
        return popt_unweighted, popt_weighted
    else:
        return None, None
