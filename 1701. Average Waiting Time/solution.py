class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        wait_time = 0
        last_finish_time = 0
        for customer in customers:
            if last_finish_time < customer[0]:
                finish_time = customer[0] + customer[1]
                wait_time += customer[1]
            else:
                finish_time = last_finish_time + customer[1]
                wait_time += last_finish_time + customer[1] - customer[0]

            last_finish_time = finish_time

        return wait_time / len(customers)
