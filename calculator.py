class Calculator(object):

    def __init__(self, num_1, num_2, op):
        self.__num_1 = num_1
        self.__num_2 = num_2
        self.__op = op

    def __add(self):
        return self.__num_1 + self.__num_2

    def __subtract(self):
        return self.__num_1 - self.__num_2

    def __multiply(self):
        return self.__num_1 * self.__num_2

    def __divide(self):
        return self.__num_1 / self.__num_2

    def calc(self):
        if "+" == self.__op:
            return self.__add()
        elif "-" == self.__op:
            return self.__subtract()
        elif "*" == self.__op:
            return self.__multiply()
        elif "/" == self.__op:
            return self.__divide()
        else:
            return "Operation not supported"
