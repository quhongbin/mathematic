def formula(n):
    """计算 1+2+3+...+n 的值"""
    return n * (n + 1) // 2

def direct_sum(n):
    """直接计算 1+2+3+...+n 的值"""
    return sum(range(1, n + 1))

# 验证基础情况
n = 1
print(f"n={n}: 公式结果 = {formula(n)}, 直接计算 = {direct_sum(n)}")

# 验证归纳步骤：假设 n=k 成立，检查 n=k+1 是否成立
for k in range(1, 10):
    # 假设公式对 n=k 成立
    assumed_value = formula(k)
    actual_value_k = direct_sum(k)
    
    # 计算 n=k+1 的值
    value_k_plus_1_formula = formula(k + 1)
    value_k_plus_1_direct = direct_sum(k + 1)
    
    # 检查归纳步骤
    if value_k_plus_1_formula == value_k_plus_1_direct:
        print(f"从 n={k} 到 n={k+1}: 归纳步骤成立")
    else:
        print(f"从 n={k} 到 n={k+1}: 归纳步骤不成立")
        break

print("\n数学归纳法验证完成！")