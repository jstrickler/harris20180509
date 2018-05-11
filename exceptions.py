#!/usr/bin/env python


class HarrisError(Exception):
    pass


x_value = 25.34

y_values =  [5.2, 'abc', 8.9, 3.38, 0, -23.1]


for y in y_values:
    try:
        result = x_value / y
    except ZeroDivisionError as err:
        print('=' * 10)
        print(err, repr(err))
        print(dir(err))
        print('=' * 10)
    # except TypeError as err:
    #     print(err)
    except (IndexError, KeyError) as err:
        pass
    except Exception as err:
        print(err)
    else:
        print(result)

    finally:
        print("***")


def spam():
    print("HELLO")
    raise HarrisError("AAARRRGGGGHHH")
    print("GOODBYE")



try:
    spam()
except HarrisError as err:
    print(err)
    # raise   re-raise exception

