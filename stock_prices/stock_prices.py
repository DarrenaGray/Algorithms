#!/usr/bin/python

import argparse

price = [100, 90, 80, 50, 20, 10]


def find_max_profit(prices):
    # Write a loop that goes over each element in a list
    # Track current min price and max profit
    # Max profit is the difference between the smallest and largest prices left of the max
    current_min_price_so_far = prices[0]  # Price at first index
    # max_price = 0
    # Price of the second index minus the current min. Initial instance will be between 0 and 1
    max_profit = prices[1] - current_min_price_so_far

    for i in range(1, len(prices)):
        print(f"Price is {prices[i]}")
        print(f"Current min price is {current_min_price_so_far}")
        # Comapre price at i index with current min price
        # Max profit is the difference between a price and the current smallest price
        # If the difference is greater than the current max profit then the difference replaces the max profit
        if prices[i] - current_min_price_so_far > max_profit:
            max_profit = prices[i] - current_min_price_so_far
        # If price[i] is less than current price then it becomes  current min price
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
    # Return the max profit
    return max_profit


print(find_max_profit(price))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

    # for i in range(0, len(prices)):
    #     # print(prices[i])
    #     for j in range(i + 1, len(prices)):
    #         # print(prices[j])
    #         if prices[i] > prices[j]:
    #             print(current_min_price_so_far)
    #             current_min_price_so_far = prices[j]
    #             print(f"Current min {current_min_price_so_far}")
    #         # elif prices[i] - current_min_price_so_far < max_profit:
    #         # print(f"Price[i] is {price[i]}")
    #         # print(f"Current min is {current_min_price_so_far}")
    #             max_profit = prices[j]-prices[i]
    #             print(f"Max profit is {max_profit}")
