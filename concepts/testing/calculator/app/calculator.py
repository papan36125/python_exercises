import pdb

class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            # print('X is: {}'.format(x))
            # print('Y is: {}'.format(y))
            # pdb.set_trace()
            result = x + y
            # print('Result is: {}'.format(result))
            return result
        else:
            raise ValueError
