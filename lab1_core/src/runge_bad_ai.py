import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def true_physics_function(x):
    return 1.0 / (1.0 + x**2)

def bad_ai_interpolation():
    x_data = np.linspace(-5, 5, 11)
    y_data = true_physics_function(x_data)
    
    x_test = 4.5
    y_true = true_physics_function(x_test)
    
    # TODO 1: 将插值方法替换为更稳定的方案（推荐 cubic spline）
    spline_interpolator = None
    # TODO 2: 计算 x_test 处预测值
    y_pred = None
    
    error = abs(y_pred - y_true)
    return error

if __name__ == "__main__":
    error = bad_ai_interpolation()
    print(f"在 x=4.5 处的插值绝对误差为: {error:.4f}")
