light = input("what light you see : ")

match light:
    case 'green':
        print('green')
    case 'yellow':
        print('yellow')
    case 'red':
        print('red')
    case _:
        print('there is no such light')