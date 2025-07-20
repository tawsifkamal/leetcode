"""
Rate Limiter Implementation using Sliding Window

This module implements a rate limiter that allows maximum N requests per 
time window using a sliding window approach with deque data structure.

Algorithm: Sliding window with timestamp tracking
Time Complexity: O(1) amortized for shouldAllowRequest
Space Complexity: O(window_size)

Author: Leetcode Practice
"""

from collections import deque



class RateLimiter:
    """
    Design a rate limiter that:
      - Allows maximum 100 requests per 10 seconds window (window gives away the fact that it can be sliding window, queue)
      - Returns true if request can be processed
      - Returns false if rate limit is exceeded
      - After 10 seconds, old requests should expire and no longer count towards limit

    Example:
      Input: timestamp = 1, output: true (1st request) since things are coming in ORDER we can put it in a queue
      Input: timestamp = 2, output: true (2nd request)
      Input: [many requests...]
      Input: timestamp = 5, output: false (exceeded 100 requests)
      Input: timestamp = 15, output: true (requests from timestamp 1-5 expired) 
    
      [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10, 11]
      # somehow keep track of the length and we need to ENSURE that len(request_window) < 100 AND window[-1] - window[0] (10 - 0) <= 10 thus we can still process this request
      # does 0 second count?
      # so basically, if it does come to a case where the NEXT timestamp - window[0] > 10 AND len(window) == 100, THEN We throw and ERROR

      # if timestamp - window[0] < 10 AND len(window) < 100, (less than 100 requests AND still valid window!!) THEN we can have requests keep coming in!!!
      # if timestamp - window[0] < 10 AND len(window) > 100, (greater than 100 requests on valid window!!) THEN we can't have any more requests keep coming in!!!
      # if timestamp - window[0] > 10 AND len(window) < 100, (not a valid window anymore so FIRST we are going to evict from beginning), WE CAN HAVE REQUESTS COMING in (add to back)
      # if timestamp - window[0] > 10 AND len(window) > 100, (this means it's 101st element) SO we are GOING to evict from the beginning, AND we are going to process this request because it would be the 100th request!!!!
    """
    def __init__(self):
        # Initialize your data structure here
        self.q = deque()  # O(1) for popleft()

    def shouldAllowRequest(self, timestamp: int) -> bool:
      # Your code here
      # edge cases is what if window is empty! then we just add
      # what if timestamp is negative? we must ensure that timestamp isn't negative!!!
      if len(self.q) == 0:
        self.q.append(timestamp)
        return True
      

      if timestamp < 0:  # handle negative timestamps
        return False
      if self.q and timestamp < self.q[-1]:  # non-chronological order
        return False
      
      
      while self.q and timestamp - self.q[0] > 9:
        # we have to keep removing invalid cases!!!!
        self.q.popleft()

      # basically ONLY 1 case where we would return FALSE. And that's when it's a VALID window BUT too many requsts!!!
      if (timestamp - self.q[0]) <= 9 and (len(self.q) >= 3):
        return False
      else:
        self.q.append(timestamp)
        return True
      
         
         
if __name__ == "__main__":
  testcases = [1, 1, 1, 11] # ALL requests PASS!!!
  

  def run_test(testcases):
    processed = []
    ratelimiter = RateLimiter()
    for timestamp in testcases:
        print(len(ratelimiter.q))
        has_processed = ratelimiter.shouldAllowRequest(timestamp)
        print((f'is_processed: {has_processed}'))
        processed.append(has_processed)   
    return processed
  
  request_statuses = run_test(testcases)
  print(f'Testcases: {testcases}')
  print(f'Request Statuses: {request_statuses}')
  


      
         