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

    # TODO 1: 计算两台望远镜波长的重叠区间上下界
    common_min = None
    common_max = None
    # TODO 2: 在重叠区间上构造统一标准网格（建议点数 >= 200）
    common_wavelength = None

    # TODO 3: 分别为 A/B 光谱构造插值器（建议 kind='cubic'）
    interpolator_A = None
    interpolator_B = None

    # TODO 4: 将 A/B 光谱都重采样到 common_wavelength
    flux_A_common = None
    flux_B_common = None

    # TODO 5: 构造合成光谱（例如简单平均或加权平均）
    fused_flux = None

    return common_wavelength, flux_A_common, flux_B_common, fused_flux

if __name__ == "__main__":
    w_common, f_A_common, f_B_common, f_fused = resample_spectra()
    if w_common is not None:
        print("光谱重采样成功！")
