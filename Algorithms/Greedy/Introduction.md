# Greedy Algorithms
- Are a class of algorithms that make locally optimal choices at each step ith the hope of finding a global optimum solution.
- At every step of the algorithm, we make a choice that looks the best at the moment.
- To make the choice, we sometimes sort the array so that we can always get the next optimal choice quickly.
- We sometimes also use a priority queue to get the next optimal item.
- After making a choice, we check for constraints (if there are any) and keep picking until we find the solution.
- Greedy algorithms do not always give the best solution.
- For example, in coin change and 0/1 knapsack problems, we get the best solution using Dynamic Programming.
- Some popular Greedy Algorithms are - **Fractional Knapsack, Dijkstra's Algorithm, Kruskal's Algorithm, Huffman coding, Prim's Algorithm**
- We get an approximately optimal solution.

## Coin Change Problem
Let's say you have a set of coins with values `[1, 2, 5, 10]`.
You need to give minimum number of coins to someone a change for 39.
```
Step 01: Start with the Largest coin value that is less than or equal to the amount to be chnaged.
Step 02: Subtract the largest coin value from the amount to be changed, and add the coin to the solution.
Step 03: Repeat the process until the amount to be changed becomes 0.
```
- The code below gives the implementation of the solution.

```python
def minCoins(coins, amount):
  coins.sort(reverse=True)
  result = []

  for coin in coins:
    while amount >= coin:
      amount = amount - coin
      resulta.ppend(coin)

  if amount != 0:
    print("Change cannpt be made with given denominations.")
    return None

  return result

# Example usage:
coins = [1, 5, 10, 25]
amount = 63

change = greedy_coin_change(coins, amount)
if change:
    print(f"Coins used: {change}")
    print(f"Total coins: {len(change)}")
```
## Why Greedy is not Optimal?
- When using the greedy approach to make change for the amount 20 with the coin denominations [18, 1, 10], the algorithm starts by selecting the largest coin value that is less than or equal to the target amount.
- In this case, the largest coin is 18, so the algorithm selects one 18 coin.
- After subtracting 18 from 20, the remaining amount is 2.
- At this point, the greedy algorithm chooses the next largest coin less than or equal to 2, which is 1.
- It then selects two 1 coins to make up the remaining amount.
- So, the greedy approach results in using one 18 coin and two 1 coins.
- However, the greedy approach fails to find the optimal solution in this case.
- Although it uses three coins, a better solution would have been to use two 10 coins, resulting in a total of only two coins (10 + 10 = 20).
