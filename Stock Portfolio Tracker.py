# Stock Portfolio Tracker

# Create a stock portfolio tracking tool that allows users
# to add, remove, and track the performance of their
# stock investments. Utilize financial APIs for real-time stock data.



import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity
               
        else:
            print("Stock not found in portfolio.")

    def track_performance(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period="1d")["Close"].iloc[-1]
            total_value += current_price * quantity
            print(f"{symbol}: {quantity} shares, Current Price: ${current_price:.2f}")

        print(f"Total Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
            print(f"{quantity} shares of {symbol} added to portfolio.")

        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
            

        elif choice == '3':
            portfolio.track_performance()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
