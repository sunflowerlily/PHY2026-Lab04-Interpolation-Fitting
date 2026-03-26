import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from galaxy_spectra import resample_spectra

def test_galaxy_spectra_resample():
    w_common, f_A_common, f_B_common, f_fused = resample_spectra()

    assert w_common is not None, "TODO 未完成：尚未构造共同波长网格"
    assert f_A_common is not None, "TODO 未完成：尚未将望远镜 A 重采样到共同网格"
    assert f_B_common is not None, "TODO 未完成：尚未将望远镜 B 重采样到共同网格"
    assert f_fused is not None, "TODO 未完成：尚未构造合成光谱"

    assert len(w_common) > 100, "共同网格点数过少，建议使用足够密集的采样"
    assert np.min(w_common) >= 4050, "共同网格应在重叠区间内，不应小于 4050"
    assert np.max(w_common) <= 6950, "共同网格应在重叠区间内，不应大于 6950"

    assert len(f_A_common) == len(w_common), "A 重采样结果长度与共同网格不一致"
    assert len(f_B_common) == len(w_common), "B 重采样结果长度与共同网格不一致"
    assert len(f_fused) == len(w_common), "合成光谱长度与共同网格不一致"

    idx_5000 = np.argmin(np.abs(w_common - 5000))
    idx_6563 = np.argmin(np.abs(w_common - 6563))

    assert f_A_common[idx_5000] < 0.7, "A 光谱在 5000 埃处吸收特征丢失"
    assert f_B_common[idx_5000] < 0.75, "B 光谱在 5000 埃处吸收特征丢失"
    assert f_fused[idx_5000] < 0.75, "合成光谱在 5000 埃处吸收特征丢失"

    assert f_A_common[idx_6563] < 0.85, "A 光谱在 6563 埃处吸收特征丢失"
    assert f_B_common[idx_6563] < 0.9, "B 光谱在 6563 埃处吸收特征丢失"
    assert f_fused[idx_6563] < 0.9, "合成光谱在 6563 埃处吸收特征丢失"
