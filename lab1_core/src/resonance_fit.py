import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def breit_wigner(E, f_r, E_r, Gamma):
    return f_r / ((E - E_r)**2 + Gamma**2 / 4)

def fit_resonance_data():
    E_data = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200], dtype=float)
    g_data = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7], dtype=float)
    
    initial_guess = [100000, 75, 50]
    
    # 学生修复后的代码
    popt, pcov = curve_fit(breit_wigner, E_data, g_data, p0=initial_guess)
    
    if popt is not None:
        f_r_fit, E_r_fit, Gamma_fit = popt
        return E_r_fit, Gamma_fit
    else:
        return None, None

if __name__ == "__main__":
    E_r_fit, Gamma_fit = fit_resonance_data()
    if E_r_fit is not None:
        print(f"拟合结果: 共振峰位置 E_r = {E_r_fit:.2f} MeV, 半高全宽 Gamma = {Gamma_fit:.2f} MeV")
