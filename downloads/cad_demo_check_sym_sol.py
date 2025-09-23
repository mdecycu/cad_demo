import cmath

x = 200
y = 230

def to_deg(rad):
    return rad * 180. / cmath.pi
# 為了與 .gif 模擬對應, 從 cad_demo_sym_formulation 得到的結果
# Sol 1 與 Sol 2 對調, Sol 3 與 Sol 4 對調
# Solution 1:
def t1_sol1(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))
def t2_sol1(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))

# Solution 2:
def t1_sol2(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))
def t2_sol2(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))

# Solution 3:
def t1_sol3(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))
def t2_sol3(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))

# Solution 4:
def t1_sol4(x, y): return 2 * cmath.atan((320*y + cmath.sqrt(-x**4 - 2*x**2*y**2 + 102400*x**2 - y**4 + 102400*y**2)) / (x**2 + 320*x + y**2))
def t2_sol4(x, y): return 2 * cmath.atan((320*y - cmath.sqrt(-x**4 + 800*x**3 - 2*x**2*y**2 - 137600*x**2 + 800*x*y**2 - 8960000*x - y**4 + 22400*y**2 + 2496000000)) / (x**2 - 720*x + y**2 + 104000))

print(to_deg(t1_sol1(x, y)).real, to_deg(t2_sol1(x, y)).real)
print(to_deg(t1_sol2(x, y)).real, to_deg(t2_sol2(x, y)).real)
print(to_deg(t1_sol3(x, y)).real, to_deg(t2_sol3(x, y)).real)
print(to_deg(t1_sol4(x, y)).real, to_deg(t2_sol4(x, y)).real)