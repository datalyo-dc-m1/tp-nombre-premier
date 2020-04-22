class Number:
    def __init__(self,number=1):
        self.number = int(number)

    def is_divisible(self,i=1):
        return self.number % i == 0

    def is_prime(self):
        num = self.number
        j = True
        if num % 2 == 0 and num != 2:
            j = False
        else:
            if num > 1:
                for i in range(2, num // 2 + 1):
                    if num % i == 0:
                        j = False
            else:
                j = False
        return j



