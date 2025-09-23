# pip install sympy
import sympy as sp

# 定義符號
x, y = sp.symbols('x y', real=True)
L = 160  # 連桿長度
B = 200  # 馬達間距

# 定義角度符號
'''
定義左馬達與右馬達的角度為符號變數：t1 與 t2（角度為徑度制，從正 X 軸起算，逆時針為正）
'''
t1, t2 = sp.symbols('t1 t2', real=True)

# 左馬達在 (0,0)
# 左側第一段連桿末端點的位置：A = (L*cos(t1), L*sin(t1))
# 第二段連桿起端點(亦即 A 點)與末端點 (x, y) 的距離應為 L：|A - (x, y)| = L

eq1 = sp.Eq((L*sp.cos(t1) - x)**2 + (L*sp.sin(t1) - y)**2, L**2)

# 右馬達在 (B, 0)
# 右側第一段連桿末端點的位置：B = (B - L*cos(t2), L*sin(t2))
# 第二段連桿末端點(亦即 B 點)與末端點 (x, y) 的距離也應為 L：|B - (x, y)| = L

eq2 = sp.Eq((B - L*sp.cos(t2) - x)**2 + (L*sp.sin(t2) - y)**2, L**2)

# 解這兩個方程組（注意，可能會有四組解）
solutions = sp.solve([eq1, eq2], (t1, t2), dict=True)

'''
# 精簡顯示所有解
for i, sol in enumerate(solutions):
    print(f"Solution {i+1}:")
    sp.pprint(sol)
    print()
'''
# 輸出符合 MathJax 格式的 LaTeX
for i, sol in enumerate(solutions):
    print(f"Solution {i+1}:\n")

    for var, expr in sol.items():
        # 建立等式 t1 = ...
        latex_str = sp.latex(sp.Eq(var, expr), mode='plain')
        print(f"\\[\n{latex_str}\n\\]\n")

# 加入指定點 (x, y) = (200, 230) 時的角度數值解
# =========================================

# 代入座標
x_val = 200
y_val = 230

# 將方程式代入特定點求數值解
eq1_num = eq1.subs({x: x_val, y: y_val})
eq2_num = eq2.subs({x: x_val, y: y_val})

# 嘗試提供兩個猜測值對，對應於 t1 和 t2
num_solutions = sp.nsolve([eq1_num, eq2_num], (t1, t2), [1.0, 1.0], dict=True)

# 輸出求得的角度（以 degree 表示）
print("Plotter 到達點 (200, 230) 時的 t1 與 t2 角度（degree）:")
for i, sol in enumerate(num_solutions):
    print(f"\nSolution {i+1}:")
    for var, val in sol.items():
        deg = sp.deg(val.evalf())
        print(f"{var} = {deg:.2f}°")