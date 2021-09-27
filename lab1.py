import sys
import math

def get_coef(index, prompt):
    '''
 Читаем коэффициент из командной строки или вводим с клавиатуры
 Args:
 index (int): Номер параметра в командной строке
 prompt (str): Приглашение для ввода коэффицента
 Returns:
 float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        coef_str = "Flag"
    while(isinstance(coef_str,str)==True):
        try:
            coef_str=float(coef_str)
        except:
            print(prompt)
            coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        if (-b / (2.0*a))>0:
            root01 = math.sqrt(-b / (2.0*a))
            root02 = -math.sqrt(-b / (2.0*a))
            result.append(root01)
            result.append(root02)
        if (-b / (2.0*a))==0:
            root00=0
            result.append(root00)
    elif D > 0.0:
        sqD = math.sqrt(D)
        if ((-b + sqD) / (2.0*a))>0:
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root3 = -math.sqrt((-b + sqD) / (2.0*a))
            result.append(root1)
            result.append(root3)
        elif ((-b + sqD) / (2.0*a))==0:
            root00=0
            result.append(root00)
        if ((-b - sqD) / (2.0*a))>0:
            root2 = math.sqrt((-b - sqD) / (2.0*a))
            root4 = -math.sqrt((-b - sqD) / (2.0*a))
            result.append(root2)
            result.append(root4)
        elif ((-b - sqD) / (2.0*a))==0:
            root00=0
            result.append(root00)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a==0:
        if b == 0:
            if c==0:
                print("Бесконечное число корней")
            else:
                print("Корней нет")
        else:
            if (-c/b)>0:
                print("Два корня: " + str(math.sqrt(-c/b)) +" и "+ str(-math.sqrt(-c/b)))
            elif abs(-c/b)==0:
                print("Два одинаковых корня: 0")
            else:
                print("Корней нет")
    else:
        # Вычисление корней
        roots = get_roots(a,b,c)
        # Вывод корней
        len_roots = len(roots)
        if len_roots == 0:
            print('Нет корней')
        elif len_roots == 1:
            print('Корни: {}'.format(roots[0]))
        elif len_roots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif len_roots == 3:
            print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
        elif len_roots == 4:
            print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
