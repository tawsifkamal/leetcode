def currencyConversion(rates, fromToArray):
    # rates is (2d array)
    # convert the array into an adjacency list where [from, to] is converted
    # run dfs on it

    rateGraph = {}
    vs = set()

    for rate in rates:
        fromCurrency = rate[0]
        toCurrency = rate[1]
        conversionRate = rate[2]

        if rateGraph.get(fromCurrency) is None:
            rateGraph[fromCurrency] = {toCurrency: conversionRate}
        else:
            rateGraph[fromCurrency][toCurrency] = conversionRate

        if rateGraph.get(toCurrency) is None:
            rateGraph[toCurrency] = {fromCurrency: 1 / conversionRate}
        else:
            rateGraph[toCurrency][toCurrency] = 1 / conversionRate

    return dfs(fromToArray[0], 1, fromToArray[1], vs, rateGraph)[1]


def dfs(node, currRate, targetNode, vs, rateGraph):
    if node in vs:
        return (False, 0)

    if node == targetNode:
        return (True, currRate)

    vs.add(node)

    for nextNode in rateGraph[node]:
        nextRate = rateGraph[node][nextNode]
        result = dfs(nextNode, currRate * nextRate, targetNode, vs, rateGraph)
        if result[0] == True:
            return result
 
    return (False, 0)

resultRate = currencyConversion(
    [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]], ['GBP', 'AUD'])

print(resultRate)
