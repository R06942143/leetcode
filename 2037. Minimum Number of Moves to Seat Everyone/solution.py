class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0

        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])

        return ans