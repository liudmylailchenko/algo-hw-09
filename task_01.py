import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    choice = [-1] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                choice[j] = coin

    result = {}
    while amount > 0:
        coin = choice[amount]
        if coin == -1:
            return {}
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


amount_test = 10000

start_greedy = time.time()
greedy_result = find_coins_greedy(amount_test)
greedy_time = time.time() - start_greedy

start_dp = time.time()
dp_result = find_min_coins(amount_test)
dp_time = time.time() - start_dp

print(f"Greedy result: {greedy_result}, Time: {greedy_time:.6f} sec")
print(f"DP result: {dp_result}, Time: {dp_time:.6f} sec")
