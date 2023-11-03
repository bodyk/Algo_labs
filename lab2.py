def min_price(product_prices, discount):
    discounted_count = len(product_prices) / 3
    min_sum = 0
    product_prices.sort(reverse=True)
    for idx, x in enumerate(product_prices):
        if (idx + 1 <= discounted_count):
            min_sum += round(x * ((100 - discount) / 100), 2)
        else:
            min_sum += x

    return min_sum