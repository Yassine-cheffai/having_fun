class Solution():
    @staticmethod
    def problem_2():
        i = 1
        while i <= 5:
            print(" ".join([str(j) for j in range(1, i+1)]))
            i += 1


Solution.problem_2()
