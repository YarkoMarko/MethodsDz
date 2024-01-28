class Convertor:
    amount_of_op = 0

    @staticmethod
    def to_celsius(fahrenheit):
        Convertor.increase()
        print(f"Amount of operations: {Convertor.amount_of_op}")
        return (fahrenheit - 32) / 1.8

    @staticmethod
    def to_fahrenheit(celsius):
        Convertor.increase()
        print(f"Amount of operations: {Convertor.amount_of_op}")
        return celsius * 1.8 + 32

    @classmethod
    def increase(cls):
        cls.amount_of_op += 1


print(Convertor.to_fahrenheit(100))