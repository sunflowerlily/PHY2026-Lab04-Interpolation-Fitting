import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def resample_spectra():
    wavelength_A = np.linspace(4000, 7000, 300)
    flux_A = 1.0 - 0.5 * np.exp(-((wavelength_A - 5000) / 50)**2) - 0.3 * np.exp(-((wavelength_A - 6563) / 30)**2)
    
    wavelength_B = np.linspace(4050, 6950, 80)
    flux_B = 1.0 - 0.45 * np.exp(-((wavelength_B - 5000) / 50)**2) - 0.28 * np.exp(-((wavelength_B - 6563) / 30)**2)
    np.random.seed(42)
    flux_B += np.random.normal(0, 0.02, size=len(wavelength_B))
    
    # 学生修复后的代码
    interpolator_B = interp1d(wavelength_B, flux_B, kind='cubic', fill_value="extrapolate")
    flux_B_resampled = interpolator_B(wavelength_A)
    
    return wavelength_A, flux_A, wavelength_B, flux_B, flux_B_resampled

if __name__ == "__main__":
    w_A, f_A, w_B, f_B, f_B_resampled = resample_spectra()
    if not np.all(f_B_resampled == 0):
        print("光谱重采样成功！")
