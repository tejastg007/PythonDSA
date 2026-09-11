class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse = s[::-1].strip()
        i = 0
        length = 0
        while i < len(reverse) and reverse[i] != ' ':
            length = length+1
            i = i+1
        return length


s = Solution()
# user will enter as many as values from the input and send them onen by one to the function
inputs = []


while True:
    value = input()
    if value.strip() == "":
        break
    inputs.append(value)

for i in inputs:
    print(s.lengthOfLastWord(i))
