from dis import dis

def say_hi():
    a = 'Привет я из функции во втором модуле'
    print('Привет я из функции во втором модуле')
    return a

dis(say_hi)