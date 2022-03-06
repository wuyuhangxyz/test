def is_prime(num):
    if num >= 0:
        if num == 1 or num == 0:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            for i in range(3,num,2):
                if num % i == 0:
                    return False
                else:
                    pass
            return True
    else:
        for i in range(num,num * -1):
            if num % i == 0:
                return False
            else:
                pass
        return True
