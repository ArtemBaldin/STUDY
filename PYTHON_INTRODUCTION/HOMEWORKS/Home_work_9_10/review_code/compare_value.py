def compare_value(sys_v, in_v):
    if in_v < sys_v:
        return 'Ваше число Меньше'
    if in_v > sys_v:
        return 'Ваше число больше'
    if in_v == sys_v:
        return 'You win!!!!'
