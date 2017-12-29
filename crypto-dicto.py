prices = { 'bitcoin': 10000, 'ethereum': 400 }
purchased = { 'bitcoin': 0.235542, 'ethereum': 0.27}

total_owed = sum(prices[currency] * purchased[currency]
                for currency in prices)

print('Oh shit I spent £{0} on magical internet monies.'.format(total_owed))
