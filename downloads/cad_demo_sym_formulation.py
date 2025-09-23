import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy as sp
import cmath

# --- 符號與逆運動學定義 ---
x, y = sp.symbols('x y', real=True)
t1, t2 = sp.symbols('t1 t2', real=True)

L = 160  # 連桿長度
B = 200  # 馬達間距

# 逆運動學方程式
eq1 = sp.Eq((L*sp.cos(t1) - x)**2 + (L*sp.sin(t1) - y)**2, L**2)
eq2 = sp.Eq((B - L*sp.cos(t2) - x)**2 + (L*sp.sin(t2) - y)**2, L**2)

# 解出所有逆運動學解（最多 4 組）
solutions = sp.solve([eq1, eq2], (t1, t2), dict=True)

# 轉為 lambda 函數列表
ik_solutions = []
for i, sol in enumerate(solutions):
    t1_expr = sol[t1]
    t2_expr = sol[t2]
    t1_func = sp.lambdify((x, y), t1_expr, 'numpy')
    t2_func = sp.lambdify((x, y), t2_expr, 'numpy')
    ik_solutions.append((t1_func, t2_func))

# --- 列印 Python math 格式方程式 ---
def print_equations():
    """將四種逆運動學解的方程式列印為 Python 程式碼格式"""
    print("--- 逆運動學解的 Python 程式碼 (使用 cmath 模組) ---")

    # 根據提供的 MathJax 格式手動轉換為 Python cmath 程式碼
    # 使用 cmath 以處理複數解
    equations_code = [
        # Solution 1
        (
            "def t1_sol1(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))",
            "def t2_sol1(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))"
        ),
        # Solution 2
        (
            "def t1_sol2(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))",
            "def t2_sol2(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))"
        ),
        # Solution 3
        (
            "def t1_sol3(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))",
            "def t2_sol3(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))"
        ),
        # Solution 4
        (
            "def t1_sol4(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))",
            "def t2_sol4(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))"
        )
    ]

    for i, (t1_code, t2_code) in enumerate(equations_code):
        print(f"\n# Solution {i+1}:")
        print(t1_code)
        print(t2_code)
    print("---------------------------------------")

print_equations()

# --- 路徑定義：畫矩形 ---
def generate_path():
    path = []
    # 從 (0, 230) 畫到 (200, 230)
    for X in np.linspace(0, 200, 100):
        path.append((X, 230))
    # 從 (200, 230) 畫到 (200, 30)
    for Y in np.linspace(230, 30, 100):
        path.append((200, Y))
    # 從 (200, 30) 畫到 (0, 30)
    for X in np.linspace(200, 0, 100):
        path.append((X, 30))
    # 從 (0, 30) 畫到 (0, 230)
    for Y in np.linspace(30, 230, 100):
        path.append((0, Y))
    return path

path = generate_path()

# --- 畫圖初始化 ---
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

lines_left = []
lines_right = []
pen_points = []
pen_traces = []
trace_coords = [[] for _ in range(4)]

# 定義方程式字串（使用 LaTeX 格式）
equations = [
    (r"$t_{1} = 2 \operatorname{atan}{\left(\frac{320 y - \sqrt{- x^{4} - \dots}}{x^{2} + \dots} \right)}$",
     r"$t_{2} = 2 \operatorname{atan}{\left(\frac{320 y - \sqrt{- x^{4} + \dots}}{x^{2} - \dots} \right)}$"),
    (r"$t_{1} = 2 \operatorname{atan}{\left(\frac{320 y - \sqrt{- x^{4} - \dots}}{x^{2} + \dots} \right)}$",
     r"$t_{2} = 2 \operatorname{atan}{\left(\frac{320 y + \sqrt{- x^{4} + \dots}}{x^{2} - \dots} \right)}$"),
    (r"$t_{1} = 2 \operatorname{atan}{\left(\frac{320 y + \sqrt{- x^{4} - \dots}}{x^{2} + \dots} \right)}$",
     r"$t_{2} = 2 \operatorname{atan}{\left(\frac{320 y - \sqrt{- x^{4} + \dots}}{x^{2} - \dots} \right)}$"),
    (r"$t_{1} = 2 \operatorname{atan}{\left(\frac{320 y + \sqrt{- x^{4} - \dots}}{x^{2} + \dots} \right)}$",
     r"$t_{2} = 2 \operatorname{atan}{\left(\frac{320 y + \sqrt{- x^{4} + \dots}}{x^{2} - \dots} \right)}$")
]

# 取得每個子圖的座標
pos = [(0.05, 0.45), (0.55, 0.45), (0.05, 0), (0.55, 0)]

for i in range(4):
    ax = axes[i]
    ax.set_title(f"Solution {i+1}")
    ax.set_xlim(-100, 300)
    ax.set_ylim(-100, 300)
    ax.set_aspect('equal')
    ax.grid(True)

    # 顯示方程式在子圖下方
    fig.text(pos[i][0], pos[i][1], equations[i][0], fontsize=8, ha='left')
    fig.text(pos[i][0], pos[i][1]-0.05, equations[i][1], fontsize=8, ha='left')

    line_left, = ax.plot([], [], 'ro-', lw=2)
    line_right, = ax.plot([], [], 'bo-', lw=2)
    pen_point, = ax.plot([], [], 'go', markersize=4)
    pen_trace, = ax.plot([], [], 'g--', lw=1, alpha=0.5)

    lines_left.append(line_left)
    lines_right.append(line_right)
    pen_points.append(pen_point)
    pen_traces.append(pen_trace)

    trace_coords[i] = ([], [])

def init():
    for i in range(4):
        lines_left[i].set_data([], [])
        lines_right[i].set_data([], [])
        pen_points[i].set_data([], [])
        pen_traces[i].set_data([], [])
    return lines_left + lines_right + pen_points + pen_traces

def animate(frame):
    if frame >= len(path):
        return lines_left + lines_right + pen_points + pen_traces

    xi, yi = path[frame]

    for i, (t1_func, t2_func) in enumerate(ik_solutions):
        try:
            theta1 = t1_func(xi, yi)
            theta2 = t2_func(xi, yi)

            # 左連桿
            x0, y0 = 0, 0
            x1 = L * np.cos(theta1)
            y1 = L * np.sin(theta1)
            lines_left[i].set_data([x0, x1, xi], [y0, y1, yi])

            # 右連桿
            xB, yB = B, 0
            x2 = B - L * np.cos(theta2)
            y2 = L * np.sin(theta2)
            lines_right[i].set_data([xB, x2, xi], [yB, y2, yi])

            # 筆尖
            pen_points[i].set_data([xi], [yi])

            # 軌跡
            trace_x, trace_y = trace_coords[i]
            trace_x.append(xi)
            trace_y.append(yi)
            pen_traces[i].set_data(trace_x, trace_y)

        except Exception as e:
            print(f"[Solution {i+1}] Error at frame {frame}: {e}")

    return lines_left + lines_right + pen_points + pen_traces

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=len(path), interval=30, blit=True
)

plt.suptitle("5-bar Linkage Plotter - Inverse Kinematics Simulation (Solutions 1 to 4)", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.97])

# 儲存為 .gif 檔案
ani.save('animation.gif', writer='pillow', dpi=50)

plt.show()