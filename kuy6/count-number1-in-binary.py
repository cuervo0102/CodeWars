class Solution():
    def __init__(self, nums) -> None:
        self.nums = nums


    def counting(self) -> int:
        stack = []
        while self.nums > 0: 
            bianry_number = self.nums % 2
            stack.append(bianry_number)
            self.nums = self.nums // 2


        stack.reverse()
        binary_string = ''.join(str(number) for number in stack)


        count_ones = 0
        for number in stack: 
            if number == 1 :
                count_ones += 1


        return count_ones



s = Solution(1234)
print(s.counting())