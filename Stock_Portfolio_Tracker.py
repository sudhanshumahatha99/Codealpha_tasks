stocks = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "MSFT": 300,   # Microsoft
    "GOOG": 2800   # Google
}

portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker 📈")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    elif stock in stocks:
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if stock in portfolio:
                portfolio[stock] += qty
            else:
                portfolio[stock] = qty
        except ValueError:
            print("❌ Please enter a valid number!")
    else:
        print("❌ Stock not found! Try again.")

total_value = 0
print("\n📊 Your Portfolio Summary 📊")
for stock, qty in portfolio.items():
    value = stocks[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print(f"\n💰 Total Portfolio Value: ${total_value}")

with open("portfolio.txt", "w") as f:
    f.write("📊 Portfolio Summary 📊\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares → ${stocks[stock] * qty}\n")
    f.write(f"\n💰 Total Portfolio Value: ${total_value}\n")

print("\n✅ Portfolio saved to 'portfolio.txt'")

