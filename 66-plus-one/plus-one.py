class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        maxIndex = len(digits) - 1
        newArr = []

        if digits[maxIndex] < 9:
            digits[maxIndex] += 1
            newArr = digits
            return newArr
        else:
            digits[maxIndex] = 0
            carry = 1

            while carry == 1 and maxIndex > 0:
                if maxIndex > 0:
                    maxIndex -= 1

                    if digits[maxIndex] < 9:
                        digits[maxIndex] += 1
                        carry = 0
                    else:
                        digits[maxIndex] = 0
                
                

               

            newArr = digits
            if carry == 1:
                newArr.insert(0, 1)
            return newArr
