import numpy as np
import matplotlib.pyplot as plt

# 设置字体为黑体
plt.rcParams['font.family'] = 'SimHei'

def q3a(T):
    """
    计算 3-alpha 反应速率中与温度相关的部分 q / (rho^2 Y^3)
    输入: T - 温度 (K)
    返回: 速率因子 (erg * cm^6 / (g^3 * s))
    """
    # 处理零温度和负温度的情况
    if T <= 0:
        return 0
    # 将温度转换为以 10^8 K 为单位
    T8 = T / 1e8
    return 5.09 * 1e11 * T8**(-3) * np.exp(-44.027 / T8)


def plot_rate(filename="rate_vs_temp.png"):
    """绘制速率因子随温度变化的 log-log 图"""
    # 生成温度数据点
    temperatures = np.logspace(7, 10, 100)
    # 计算对应的速率值
    rates = [q3a(T) for T in temperatures]
    # 绘制双对数图
    plt.loglog(temperatures, rates)
    plt.xlabel('温度 (K)')
    plt.ylabel('q_3α / (ρ²Y³) (erg * cm⁶ / (g³ * s))')
    plt.title('3-α 反应速率与温度关系')
    plt.grid(True)
    plt.savefig(filename)
    plt.show()


if __name__ == "__main__":
    # 计算并打印 nu 值
    print("   温度 T (K)    :   ν (敏感性指数)")
    print("--------------------------------------")

    temperatures_K = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    h = 1.0e-8  # 扰动因子

    for T0 in temperatures_K:
        q_T0 = q3a(T0)
        # 避免 q_T0 为零的情况
        if q_T0 == 0:
            nu = 0
        else:
            delta_T = h * T0
            q_T0_plus_delta_T = q3a(T0 + delta_T)
            # 使用前向差分计算导数
            dq_dT = (q_T0_plus_delta_T - q_T0) / delta_T
            # 计算敏感性指数 nu
            nu = (T0 / q_T0) * dq_dT
        print(f"{T0:16.2e} : {nu:16.2e}")

    # 调用绘图函数展示结果
    plot_rate()
