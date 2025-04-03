def 階乘(甲):
    global 階乘

    if 甲 == 1:
        return 甲

    else:
        _ans1 = 甲-1

        乙 = _ans1
        _ans2 = 階乘(乙)

        丙 = _ans2
        _ans3 = 丙*甲

        丁 = _ans3
        return 丁


_ans4 = 階乘(5)
print(_ans4)
