def currencyConversion(rates, fromToArray):
    """
    This function calculates the conversion rate between two currencies given a
    list of exchange rates.

    Args:
      rates: A list of lists, where each inner list represents an exchange
        rate in the format [from_currency, to_currency, rate].
      fromToArray: A list containing the starting and ending currencies, in
        the format [from_currency, to_currency].

    Returns:
      The conversion rate between the two currencies, or 0 if a conversion
      is not possible.
    """
    rateGraph = {}
    vs = set()

    # Build the graph of conversion rates
    for rate in rates:
        fromCurrency = rate[0]
        toCurrency = rate[1]
        conversionRate = rate[2]

        if fromCurrency not in rateGraph:
            rateGraph[fromCurrency] = {}
        rateGraph[fromCurrency][toCurrency] = conversionRate

        if toCurrency not in rateGraph:
            rateGraph[toCurrency] = {}
        rateGraph[toCurrency][fromCurrency] = 1 / conversionRate

    # Find the conversion rate using DFS
    result = dfs(fromToArray[0], 1, fromToArray[1], vs, rateGraph)
    return result[1] if result else 0


def dfs(node, currRate, targetNode, vs, rateGraph):
    """
    This function performs a depth-first search on the currency graph to find
    the conversion rate.

    Args:
      node: The current currency node in the graph.
      currRate: The current conversion rate from the starting currency.
      targetNode: The target currency to convert to.
      vs: A set of visited nodes to prevent cycles.
      rateGraph: The graph of conversion rates.

    Returns:
      A tuple containing a boolean indicating if a path was found, and the
      final conversion rate. Returns None if no path is found.
    """
    if node in vs:
        return None

    if node == targetNode:
        return (True, currRate)

    vs.add(node)

    if node in rateGraph:
        for nextNode in rateGraph[node]:
            nextRate = rateGraph[node][nextNode]
            result = dfs(nextNode, currRate * nextRate, targetNode, vs, rateGraph)
            if result:
                return result

    return None

resultRate = currencyConversion(
    [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]], ['GBP', 'AUD'])

print(resultRate)
