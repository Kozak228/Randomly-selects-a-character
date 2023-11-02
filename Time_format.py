def add_zero(num):
    return f"0{num}" if num < 10 else num

def s_in_m(all_time):
    s = all_time % 60
    m = (all_time // 60) % 60

    return s, m

def m_in_s(m, s):
    m_in_s = m * 60

    return m_in_s + s