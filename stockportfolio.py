# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 290
}

# Track portfolio
portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from available options.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Calculate and store
    investment = stock_prices[stock] * quantity
    total_investment += investment
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Display result
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ {stock_prices[stock]} = ₹{qty * stock_prices[stock]}")
print(f"💰 Total Investment: ₹{total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("📊 Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares @ {stock_prices[stock]} = ₹{qty * stock_prices[stock]}\n")
        file.write(f"\n💰 Total Investment: ₹{total_investment}")
    print("✅ Summary saved to 'portfolio_summary.txt'")
