# problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return
        mapping = [
            "0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.letterCombinationsRecursive(result, digits, "", 0, mapping)
        return result

    def letterCombinationsRecursive(self, result, digits, current, index, mapping):
        if len(digits) == index:
            result.append(current)
            return
        letters = mapping[int(digits[index])]
        for i in range(len(letters)):
            self.letterCombinationsRecursive(result, digits,current+letters[i], index+1, mapping)