"""
Stock Portfolio Tracker
A simple program to calculate total investment based on stock prices
"""

def get_stock_data():
    """Get stock names and quantities from user"""
    stocks = {}
    print("=== Stock Portfolio Tracker ===\n")
    
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").strip().upper()
        
        if stock_name.lower() == 'done':
            break
        
        if not stock_name:
            print("Stock name cannot be empty. Please try again.\n")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.\n")
                continue
            stocks[stock_name] = quantity
            print(f"✓ Added {quantity} shares of {stock_name}\n")
        except ValueError:
            print("Invalid quantity. Please enter a number.\n")
    
    return stocks

def get_stock_prices():
    """Get stock prices from user"""
    prices = {}
    print("\n=== Enter Stock Prices ===\n")
    
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").strip().upper()
        
        if stock_name.lower() == 'done':
            break
        
        if not stock_name:
            print("Stock name cannot be empty. Please try again.\n")
            continue
        
        try:
            price = float(input(f"Enter price for {stock_name}: $"))
            if price < 0:
                print("Price cannot be negative. Please try again.\n")
                continue
            prices[stock_name] = price
            print(f"✓ Set price for {stock_name} at ${price:.2f}\n")
        except ValueError:
            print("Invalid price. Please enter a number.\n")
    
    return prices

def calculate_portfolio_value(stocks, prices):
    """Calculate total investment value"""
    total_value = 0
    portfolio_details = []
    
    print("\n" + "="*60)
    print("PORTFOLIO SUMMARY")
    print("="*60)
    print(f"{'Stock':<15} {'Quantity':<12} {'Price':<12} {'Total Value':<15}")
    print("-"*60)
    
    for stock, quantity in stocks.items():
        if stock in prices:
            stock_value = quantity * prices[stock]
            total_value += stock_value
            portfolio_details.append({
                'stock': stock,
                'quantity': quantity,
                'price': prices[stock],
                'total': stock_value
            })
            print(f"{stock:<15} {quantity:<12} ${prices[stock]:<11.2f} ${stock_value:<14.2f}")
        else:
            print(f"{stock:<15} {quantity:<12} {'N/A':<12} {'Not priced':<15}")
    
    print("-"*60)
    print(f"{'TOTAL PORTFOLIO VALUE:':<40} ${total_value:,.2f}")
    print("="*60 + "\n")
    
    return total_value, portfolio_details

def save_to_file(stocks, prices, total_value, portfolio_details):
    """Save portfolio results to a file"""
    print("Save portfolio data:")
    print("1. Text file (.txt)")
    print("2. CSV file (.csv)")
    print("3. Skip saving")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "portfolio"
        filename += ".txt"
        
        with open(filename, 'w') as f:
            f.write("STOCK PORTFOLIO TRACKER\n")
            f.write("="*60 + "\n\n")
            f.write(f"{'Stock':<15} {'Quantity':<12} {'Price':<12} {'Total Value':<15}\n")
            f.write("-"*60 + "\n")
            
            for detail in portfolio_details:
                f.write(f"{detail['stock']:<15} {detail['quantity']:<12} "
                       f"${detail['price']:<11.2f} ${detail['total']:<14.2f}\n")
            
            f.write("-"*60 + "\n")
            f.write(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}\n")
        
        print(f"✓ Portfolio saved to {filename}")
    
    elif choice == '2':
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "portfolio"
        filename += ".csv"
        
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price,Total Value\n")
            for detail in portfolio_details:
                f.write(f"{detail['stock']},{detail['quantity']},"
                       f"{detail['price']:.2f},{detail['total']:.2f}\n")
            f.write(f"TOTAL,,,{total_value:.2f}\n")
        
        print(f"✓ Portfolio saved to {filename}")
    
    else:
        print("Portfolio not saved.")

def main():
    """Main function to run the stock portfolio tracker"""
    # Example usage with hardcoded dictionary
    print("Would you like to:")
    print("1. Use example data (AAPL: 180, TSLA: 250)")
    print("2. Enter your own data")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == '1':
        # Hardcoded example
        stocks = {"AAPL": 180, "TSLA": 250}
        prices = {"AAPL": 150.50, "TSLA": 220.75}
        print("\nUsing example data:")
        print(f"Stocks: {stocks}")
        print(f"Prices: {prices}")
    else:
        # User input
        stocks = get_stock_data()
        
        if not stocks:
            print("No stocks entered. Exiting program.")
            return
        
        prices = get_stock_prices()
        
        if not prices:
            print("No prices entered. Exiting program.")
            return
    
    # Calculate portfolio value
    total_value, portfolio_details = calculate_portfolio_value(stocks, prices)
    
    # Option to save
    save_option = input("Would you like to save the results? (yes/no): ").strip().lower()
    if save_option in ['yes', 'y']:
        save_to_file(stocks, prices, total_value, portfolio_details)
    
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
