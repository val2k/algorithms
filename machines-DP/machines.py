#!/usr/bin/python3.4


input = [(1, 9, 1, 2),
  (2, 10, 9, 1),
  (3, 2, 1, 2),
  (4, 11, 7, 4),
  (5, 0, 0, 0),
  (6, 12, 1, 3),
  (7, 0, 0, 0),
  (8, 20, 5, 4),
  (9, 0, 0, 0),
  (10, 0, 0, 0),
  (11, 0, 0, 0),
  (12, 0, 0, 0),
  (13, 0, 0, 0),
  (14, 0, 0, 0),
  (15, 0, 0, 0),
  (16, 0, 0, 0),
  (17, 0, 0, 0),
  (18, 0, 0, 0),
  (19, 0, 0, 0),
  (20, 0, 0, 0)]

memoization = {}
max_day = len(input)

def maxProfit(dollars, day, hold):
    # all actions
    sell_buy, sell, buy, skip, nothing = 0, 0, 0, 0
    
    # return the value from dictionnary if already calculed 
    if (dollars, day, hold) in memoization:
        return memoization[dollars, day, hold]
   
    # stopping criterion
    if day >= max_day:
        if hold != -1: 
            return dollars + input[hold][2]
        return dollars

    if dollars >= input[day][1] and hold == -1:
        buy = maxProfit(dollars - input[day][1], day + 1, day)
    


  
