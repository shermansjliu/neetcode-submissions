class Solution:
    def __init__(self):
        self.res = []
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digits_map = {
            "2":"abc", 
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        self.explore(digits, 0, [], digits_map)
        return self.res 

    def explore(self, digits, digit_i, state:List[str], digits_map):
        if len(state) >= len(digits):
            self.res.append("".join(state))
            return 
        for c in digits_map[digits[digit_i]]:
            state.append(c)
            self.explore(digits, digit_i+1, state, digits_map)
            state.pop()
            
        



        