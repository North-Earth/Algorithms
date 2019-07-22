class RecursiveAlgorithms():
    # Алгоритм рекурсивного суммирования чисел.
    def sum_numbers(self, collection, idx = 0):
        length = len(collection)
        id = idx + 1
        if(length == id):
            return collection[idx]
        else:
            return collection[idx] + self.sum_numbers(collection,idx)

    # Алгоритм нахождения факторила.
    def factorial(x):
        if x <= 0:
            return 1
        return x * factorial(x - 1)

    # Алгоритм нахождения числа Фибоначчи.
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)