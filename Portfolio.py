# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock:", stock)
        print("Price per share: $", stock_prices[stock])
        print("Quantity:", quantity)
        print("Investment: $", investment)

    else:
        print("Stock not available.")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write("Total Investment: $" + str(total_investment))

print("Portfolio saved to portfolio.txt")