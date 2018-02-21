"""
Calculates compound interest over a specified time period.

Since:
    1.0.0

Catergory:
    Maths

Args:
    param1 (int) investment: The amount of original investment.
    param2 (int) rate: Interest rate in whole number. i.e. 2% = 2.
    param3 (int) time: Length of investment. Used to exponentially raise total.
        Assumes interest is applied for every whole integer in param.

Returns:
    Integer: Does not round or format the returned value.

Example:
    >>> print(compound_interest(10, 3, 5))
    11.592740743000002
"""


def compound_interest(investment, rate, time):
    counter = 0
    total = investment
    interest = 1 + (rate * 0.01)

    while counter < time:
        total = total * interest
        counter += 1

    return total
