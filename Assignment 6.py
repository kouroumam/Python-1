


#Input: Ask the user to enter an amount in one currency (e.g., USD).
#Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
#Output: Display the converted amount in the target currency.


USD_TO_EUR_RATE = 0.97
amount_in_usd = float(input("Enter the amount in USD: "))

amount_in_eur = amount_in_usd * USD_TO_EUR_RATE

print("This is equal to:", round(amount_in_eur, 2), "EUR")