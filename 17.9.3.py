while True:
    try:
        numbers = input('Введите числа через пробел: ')
        number_user = int(input('Введите любое число: '))
        number_list = numbers.split()

        s = ''
        a = s.join(number_list)

        if " " not in numbers:
            print("\nВведите числа через пробел!")
            continue
        elif a.isdigit():
            break
        else:
            print('Вводить нужно только цифры')
            continue
    except ValueError:
        print("Нужно ввести число!")


number_list = list(map(int, number_list))
number_list.sort()
print(number_list)

def search(array, element):

    mid = 0
    start = 0
    end = len(array)
    error1 = array[0]
    error2 = array[-1]
    step = 0

    while start <= end:

        step = step+1
        mid = (start + end) // 2
        try:
            if element == array[mid]:
                return mid
        except IndexError:
                return False
        if element == error2:
            return False
        if element < error1:
            return False
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if len(array) // 2:
        return array[end]
    else:
        return array[start]

answer = (search(number_list, number_user))
if answer == False:
    print("Искомое число выходит за диапазон поиска")

else:
    print("номер позиции элемента, который меньше введенного числа " + str(number_list.index(answer)))
    print("Номер позиции элемента, который больше введенного числа или равен ему " + str(number_list.index(answer) + 1))


