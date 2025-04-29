def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD', 'INR', 'GBP', 'JPY', 'AUD', 'CHF', 'CNY')
    while True:
        currency = input(f'{label} currency ({"/".join(currencies)}): ').upper()
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'CAD': 1.25, 'INR': 83.0, 'GBP': 0.75, 'JPY': 110.0, 'AUD': 1.35, 'CHF': 0.91, 'CNY': 7.2},
        'EUR': {'USD': 1.18, 'CAD': 1.47, 'INR': 91.5, 'GBP': 0.88, 'JPY': 129.0, 'AUD': 1.6, 'CHF': 1.07, 'CNY': 8.4},
        'CAD': {'USD': 0.80, 'EUR': 0.68, 'INR': 62.0, 'GBP': 0.59, 'JPY': 87.0, 'AUD': 1.07, 'CHF': 0.73, 'CNY': 5.6},
        'INR': {'USD': 0.012, 'EUR': 0.011, 'CAD': 0.016, 'GBP': 0.0090, 'JPY': 1.3, 'AUD': 0.016, 'CHF': 0.011, 'CNY': 0.087},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'CAD': 1.70, 'INR': 111.0, 'JPY': 150.0, 'AUD': 1.80, 'CHF': 1.21, 'CNY': 9.5},
        'JPY': {'USD': 0.0091, 'EUR': 0.0078, 'CAD': 0.011, 'INR': 0.77, 'GBP': 0.0067, 'AUD': 0.012, 'CHF': 0.0081, 'CNY': 0.063},
        'AUD': {'USD': 0.74, 'EUR': 0.63, 'CAD': 0.93, 'INR': 61.5, 'GBP': 0.56, 'JPY': 82.0, 'CHF': 0.67, 'CNY': 5.3},
        'CHF': {'USD': 1.10, 'EUR': 0.94, 'CAD': 1.37, 'INR': 90.0, 'GBP': 0.83, 'JPY': 123.0, 'AUD': 1.48, 'CNY': 7.9},
        'CNY': {'USD': 0.14, 'EUR': 0.12, 'CAD': 0.18, 'INR': 11.5, 'GBP': 0.11, 'JPY': 16.0, 'AUD': 0.19, 'CHF': 0.13},
    }

    if source_currency == target_currency:
        return amount

    try:
        return amount * exchange_rates[source_currency][target_currency]
    except KeyError:
        print(f"Exchange rate not available for {source_currency} to {target_currency}")
        return None


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    if converted_amount is not None:
        print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')


if __name__ == "__main__":
    main()
