lass Solution:
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        
        def get_cost(digits):
            cost = 0
            curr = startAt
            
            for d in digits:
                d = int(d)
                if curr != d:
                    cost += moveCost
                cost += pushCost
                curr = d
            
            return cost
        
        res = float('inf')
        
        # Try all possible (minutes, seconds)
        for m in range(100):
            for s in range(100):
                if m * 60 + s == targetSeconds:
                    
                    # Format into string and remove leading zeros
                    time_str = f"{m:02}{s:02}".lstrip('0')
                    
                    # Edge case: if empty → means "0000"
                    if time_str == "":
                        time_str = "0"
                    
                    res = min(res, get_cost(time_str))
        
        return res
