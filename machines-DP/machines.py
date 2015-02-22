#!/usr/bin/python3.4
import re
from itertools import takewhile

memoization = {}

def maxProfit(dollars, day, hold, max_day, input):
    """ Function using dynamic programming 
    States: selling, buying, selling & buying,skipping (getting profit of the machine), or doing nothing 
    """
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
    
    # action of buying a machine
    if dollars >= input[day][1] and hold == -1:
        buy = maxProfit(dollars - input[day][1], day + 1, day, max_day, input)
    
    # action of doing nothing (if holding no machine)
    if hold == -1:
        nothing = maxProfit(dollars, day + 1, hold, max_day, input)
    
    # if we hold a machine, we can sell, sell&buy or only get the profit of the day (skip)
    elif hold != -1:
        sell = maxProfit(dollars + input[hold][2], day + 1, -1, max_day, input)
        skip = maxProfit(dollars + input[hold][3], day + 1, hold, max_day, input)
        
        # we can sell&buy only if we have enough money to buy the machine at the current day
        if dollars + input[hold][2] >= input[day][1]:
            sell_buy = maxProfit(dollars + input[hold][2] - input[day][1], day + 1, day, max_day, input)

    tmp_dollars = max(buy, nothing, sell, skip, sell_buy)
    memoization[dollars, day, hold] = tmp_dollars

    return tmp_dollars

def extract_data(filename):
    """ Extract and analyze data from file """

    data_lst = []
    with open(filename) as f:
        for line in f:
            data_lst.append(tuple(int(v) for v in re.findall("[0-9]+", line)))
    
    data = {}

    for i, val in enumerate(data_lst):
        if val == (0, 0, 0): break
        if len(val) == 3:
                   
            data[val] = (list(takewhile(lambda x: len(x) > 3, data_lst[i+1:])))
            data_dict = { d[0]: (d[0], d[1], d[2], d[3]) for d in data[val] }
            data[val] = []

            for x in range(1, val[2] + 1):
                if x in data_dict: data[val].append(data_dict[x])
                else: data[val].append((x, 0, 0, 0))    

    return data

if __name__ == "__main__":
    extracted_data = extract_data("input.txt")

    for k, v in extracted_data.items():
        print(maxProfit(k[1], 0, -1, k[2], v))
    


