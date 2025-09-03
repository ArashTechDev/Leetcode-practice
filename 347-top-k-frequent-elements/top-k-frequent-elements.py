class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        top_k = []

        for num,freq in hashMap.items():
            inserted = False
            for i in range(len(top_k)):
                if freq > top_k[i][1]:
                    top_k.insert(i,(num,freq))
                    inserted = True
                    break
            if not inserted:                    # if element was not inserted, it gets added at the end
                top_k.append((num,freq))
            
            if len(top_k) > k:                   # keep top_k with only <=k pairs
                top_k.pop()                      # remove last pair if len > k
        
        return [num for num,freq in top_k]
                
