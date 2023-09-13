if __name__ == "__main__":
    ls = [7,1,5,3,6,4]
    minPrice = ls[0]
    maxProfit = -1
    for i in ls[1:]:
        minPrice = min(minPrice, i)
        maxProfit = max(maxProfit, i - minPrice)
    print(maxProfit)