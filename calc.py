import sys

while True:
    try:
        str = input()
        if str == '':
            sys.exit()
        if str[0] != '#':
            lst = str.split('=')
            if len(lst) == 1:
               eval(str)
               print(eval(str))
            elif len(lst) == 2:
                eval(lst[0])
                exec(lst[0] + '=' + lst[1])

    except ZeroDivisionError as err:
        print(err)
    except SyntaxError as err:
        print(err)
    except IndexError as err:
        print(err)
    except Exception as err:
        print(err)

