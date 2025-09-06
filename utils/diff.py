def normalize(v):
    if v is None: return ''
    return str(v).strip()

def compare_values(old, new):
    old_n, new_n = normalize(old), normalize(new)
    if old is None and new_n != '':
        return True, f"→ now ‘{new_n}’"
    if old_n == new_n:
        return False, 'no change'
    def to_num(x):
        try: return float(x.replace('$','').replace(',',''))
        except Exception: return None
    o_num, n_num = to_num(old_n), to_num(new_n)
    if o_num is not None and n_num is not None:
        diff = n_num - o_num
        sign = '+' if diff >= 0 else '−'
        return True, f"{old_n} → {new_n} ({sign}{abs(diff):.2f})"
    return True, f"{old_n} → {new_n}"
