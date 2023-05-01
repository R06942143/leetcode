class Solution:
    def average(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)


"""
        max_salary = float("-inf")
        min_salary = float("inf")
        all_money = 0
        for money in salary:
            if money > max_salary:
                max_salary = money
            if money < min_salary:
                min_salary = money
            all_money += money
        ans = (all_money - max_salary - min_salary)/ (len(salary) - 2)
        return float(f"{ans:.5f}")
"""
