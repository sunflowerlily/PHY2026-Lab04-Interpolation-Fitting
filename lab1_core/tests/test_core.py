import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from runge_bad_ai import bad_ai_interpolation
from resonance_fit import fit_resonance_data, breit_wigner
from weighted_fit import weighted_fit

def test_runge_trap_fixed():
    """
    测试学生是否修复了 Runge 现象。
    物理验证：如果是拉格朗日多项式，误差会非常大（远大于 0.05）。
    如果换成了样条插值，误差会很小。
    """
    error = bad_ai_interpolation()
    assert error < 0.05, f"AI 毒药未完全排雷！当前误差为 {error:.4f}，这在物理上是不可接受的巨大振荡。"

def test_resonance_fit_core():
    """
    测试共振拟合是否成功提取出正确的物理参数。
    """
    # 1. 测试 Breit-Wigner 公式实现
    f_r, E_r, Gamma = 100000, 75, 50
    expected_peak = 4 * f_r / (Gamma**2)
    calculated_peak = breit_wigner(E_r, f_r, E_r, Gamma)
    assert calculated_peak is not None, "TODO 1 未完成：breit_wigner 返回了 None"
    np.testing.assert_allclose(calculated_peak, expected_peak, rtol=1e-5, err_msg="Breit-Wigner 公式实现错误")
    
    # 2. 测试拟合参数
    E_r_fit, Gamma_fit = fit_resonance_data()
    assert E_r_fit is not None, "TODO 2 未完成：未能返回 E_r_fit"
    assert 70 < E_r_fit < 85, f"拟合的共振峰位置 {E_r_fit:.2f} 不符合物理预期，应在 75 附近。"
    assert 30 < Gamma_fit < 70, f"拟合的半高全宽 {Gamma_fit:.2f} 不符合物理预期，应在 50 附近。"

def test_weighted_fit():
    """
    测试加权拟合的实现。
    加权拟合会更倾向于相信误差较小的点。
    """
    res = weighted_fit()
    assert res[0] is not None and res[1] is not None, "Task C TODO 未完成"
    
    popt_unw, popt_w = res
    
    # 检查加权和非加权拟合的参数确实有所不同
    # 由于 E=75 处的误差极大 (85.5)，而高能区的误差较小 (4.14)，
    # 加权拟合会略微“放弃”拟合峰值，而更贴合尾部，因此共振参数会有物理上的偏移。
    assert not np.allclose(popt_unw, popt_w), "加权拟合与非加权拟合参数完全一样，说明 sigma 参数未正确应用！"
