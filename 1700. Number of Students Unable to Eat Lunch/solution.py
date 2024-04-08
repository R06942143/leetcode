class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        want_zero = 0
        want_one = 0

        for student in students:
            if student == 0:
                want_zero += 1
            else:
                want_one += 1
        
        while students:
            if students[0] == sandwiches[0]:
                if students[0] == 0:
                    want_zero -= 1
                else:
                    want_one -= 1
                students = students[1:]
                sandwiches = sandwiches[1:]
                continue
            else:
                students = students[1:] + [students[0]]
            
            if (sandwiches[0] == 0 and want_zero == 0) or (sandwiches[0] == 1 and want_one == 0):
                break

        return len(students)