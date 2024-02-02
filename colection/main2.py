def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        print('корней нет')
    elif d == 0:
        return b/(2 * a)
    else:
        x1 = (b + d ** 0.5)/(2 * a)
        x2 = (-b - d ** 0.5)/(2 * a)
        return x1


# if __name__ == '__main__':
#     # print(solution(1, 8, 15))
#     # print(solution(1, 13, 12))
#     # print(solution(4, 28, 49))
#     # print(solution(1, 1, 1))
#     # print(discriminant(1, 8, 15))