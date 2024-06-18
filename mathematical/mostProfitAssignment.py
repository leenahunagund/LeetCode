class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        '''

        My soln , 3/57 test cases passed 
        
        Approach 2: Using the min() Function
        In this example, we use the min() function with a lambda function as the key. 
        The lambda function calculates the absolute difference between each element and the target value.
        The min() function then returns the element with the smallest difference, which is the closest value.
        
        target_value = 7 
        list_values = [2, 5, 8, 11, 14] 
        closest_value = min(list_values, key=lambda x: abs(x - target_value)) 
        print(f"The closest value to {target_value} is {closest_value}")

        t=0
        for i in range(len(worker)):
            if worker[i] in difficulty:
                t+=profit[difficulty.index(worker[i])]
            else:
                if
                num = min(difficulty, key=lambda x: abs(x - worker[i])) 
                t+=profit[difficulty.index(num)]
        return t'''
        jobs = sorted(zip(difficulty, profit))
        
        # Sort workers
        worker.sort()
        
        # Initialize total profit and the best profit seen so far
        total_profit = 0
        best_profit = 0
        job_index = 0
        
        # Iterate over each worker
        for ability in worker:
            # Update the best possible profit for the worker's ability
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            total_profit += best_profit
        
        return total_profit
        
