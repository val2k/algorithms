#!/usr/bin/python3.4
import re

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
    sell_buy, sell, buy, skip, nothing = 0, 0, 0, 0, 0
    
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
    
    if hold == -1:
        nothing = maxProfit(dollars, day + 1, hold)
    
    elif hold != -1:
        sell = maxProfit(dollars + input[hold][2], day + 1, -1)
        skip = maxProfit(dollars + input[hold][3], day + 1, hold)
        
        if dollars + input[hold][2] >= input[day][1]:
            sell_buy = maxProfit(dollars + input[hold][2] - input[day][1], day + 1, day)

    tmp_dollars = max(buy, nothing, sell, skip, sell_buy)
    memoization[dollars, day, hold] = tmp_dollars

    return tmp_dollars

def extract_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(tuple(int(v) for v in re.findall("[0-9]+" , line)))            
    f.close()
    return data

if __name__ == "__main__":
    print(maxProfit(10, 0, -1))
    input = extract_data("input2.txt")
    fst_line = input[0]
    data = sorted(input[1:-1])
    print(fst_line)
    print(data)
