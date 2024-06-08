class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hardworker_numbers = 0
        for i in range(len(hours)):
            if hours[i] >= target: 
                hardworker_numbers += 1
        return hardworker_numbers