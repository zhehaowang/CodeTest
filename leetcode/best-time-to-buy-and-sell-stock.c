int maxProfit(int* prices, int pricesSize) {
    int i = 0;
    int curStart = 0;
    int curEnd = pricesSize - 1;
    
    int s = 0;
    int e = pricesSize - 1;
    int profit = prices[curEnd] - prices[curStart];    

    while (s < e - 1) {
        if (prices[s] - prices[s + 1] > prices[e - 1] - prices[e]) {
            if (prices[curEnd] - prices[s + 1] > profit) {
                curStart = s + 1;
                profit = prices[curEnd] - prices[curStart];
            }
            s = s + 1;
        } else {
            if (prices[e - 1] - prices[curStart] > profit) {
                curEnd = e - 1;
                profit = prices[curEnd] - prices[curStart];
            }
            e = e - 1;
        }
    }
    if (profit > 0) {
        return profit;
    } else {
        return 0;
    }
}

int main() {
    int prices[7] = {2, 1, 2, 1, 0, 1, 2};
    int profit = maxProfit(prices, 7);
    printf("Max profit is %d.\n", profit);
    return 1;
}
