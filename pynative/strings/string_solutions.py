class Solution:
    @staticmethod
    def isprime(number: int) -> bool:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def problem_2():
        i = 1
        while i <= 5:
            print(" ".join([str(j) for j in range(1, i + 1)]))
            i += 1

    @staticmethod
    def problem_3(n: int):
        sum = 0
        for i in range(n + 1):
            sum += i
        return sum

    @staticmethod
    def problem_4():
        for i in range(1, 11):
            print(i * 2)

    @staticmethod
    def problem_5(numbers: list):
        for number in numbers:
            if number > 500:
                break
            if number % 5 == 0 and number <= 150:
                print(number)

    @staticmethod
    def problem_6(number: int):
        return len(str(number))

    @staticmethod
    def problem_7():
        for i in reversed(range(1, 6)):
            print(" ".join([str(i) for i in reversed(range(1, i + 1))]))

    @staticmethod
    def problem_8(l: list):
        for item in reversed(l):
            print(item)

    @staticmethod
    def problem_9():
        for number in reversed(range(1, 11)):
            print(-number)

    @staticmethod
    def problem_10():
        for i in range(6):
            print(i)
        else:
            print("Done!")

    @staticmethod
    def problem_11(start: int, end: int) -> list:
        result = []
        for i in range(start, end + 1):
            if Solution.isprime(i):
                result.append(i)

        return result

    @staticmethod
    def problem_12() -> list:
        result = [0, 1]
        while len(result) < 10:
            last_index = len(result) - 1
            new_value = result[last_index] + result[last_index - 1]
            result.append(new_value)

        return result
