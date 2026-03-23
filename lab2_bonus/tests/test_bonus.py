import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from galaxy_spectra import resample_spectra

def test_galaxy_spectra_resample():
    """
    测试 Bonus: 光谱是否被正确插值到了新网格上。
    """
    w_A, f_A, w_B, f_B, f_B_resampled = resample_spectra()
    
    assert not np.all(f_B_resampled == 0), "TODO 未完成：重采样的光谱全是 0"
    assert len(f_B_resampled) == len(w_A), "重采样的数组长度不等于标准网格长度！"
    
    # 检查吸收线是否在 5000 和 6563 附近正确出现
    idx_5000 = np.argmin(np.abs(w_A - 5000))
    idx_6563 = np.argmin(np.abs(w_A - 6563))
    
    # 在吸收线中心，通量应该明显下降（低于背景 1.0）
    assert f_B_resampled[idx_5000] < 0.7, "重采样失败：5000 埃处的物理吸收特征丢失！"
    assert f_B_resampled[idx_6563] < 0.85, "重采样失败：6563 埃处的物理吸收特征丢失！"
