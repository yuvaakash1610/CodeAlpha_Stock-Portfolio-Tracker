# Stock Portfolio Tracker 📈

A simple command-line Python application that helps you track your stock investments and calculate total portfolio value.


## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Key Concepts](#key-concepts)
- [Sample Output](#sample-output)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- 

## 🎯 About

This Stock Portfolio Tracker is a beginner-friendly Python project designed to help you calculate the total value of your stock investments. It demonstrates fundamental programming concepts including dictionaries, input/output operations, basic arithmetic, and file handling.

Perfect for Python learners who want to build practical, real-world applications!

## ✨ Features

- **📊 Portfolio Management** - Track multiple stocks with their quantities
- **💰 Value Calculation** - Automatically calculates total investment value
- **📝 Input Validation** - Handles invalid user inputs gracefully
- **💾 Export Options** - Save results to `.txt` or `.csv` files
- **🎨 Formatted Output** - Clean, table-style display of portfolio data
- **🔧 Flexible Input** - Use example data or enter your own
- **📈 Summary View** - See all stocks and total value at a glance

## 🛠️ Technologies Used

- **Python 3.6+**
- Standard Library modules:
  - Built-in file handling
  - String formatting
  - Error handling with try-except

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system
- Basic understanding of command-line operations

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/stock-portfolio-tracker.git
```

2. Navigate to the project directory
```bash
cd stock-portfolio-tracker
```

3. Run the program
```bash
python stock_tracker.py
```

That's it! No external dependencies required. 🎉

## 📖 How to Use

### Option 1: Use Example Data

```
Would you like to:
1. Use example data (AAPL: 180, TSLA: 250)
2. Enter your own data

Enter your choice (1 or 2): 1
```

The program will use predefined stock data to demonstrate functionality.

### Option 2: Enter Your Own Data

```
Enter your choice (1 or 2): 2

=== Stock Portfolio Tracker ===

Enter stock name (or 'done' to finish): AAPL
Enter quantity for AAPL: 180
✓ Added 180 shares of AAPL

Enter stock name (or 'done' to finish): TSLA
Enter quantity for TSLA: 250
✓ Added 250 shares of TSLA

Enter stock name (or 'done' to finish): done

=== Enter Stock Prices ===

Enter stock name (or 'done' to finish): AAPL
Enter price for AAPL: $150.50
✓ Set price for AAPL at $150.50

Enter stock name (or 'done' to finish): TSLA
Enter price for TSLA: $220.75
✓ Set price for TSLA at $220.75

Enter stock name (or 'done' to finish): done
```

### View Results

The program displays a formatted summary:

```
============================================================
PORTFOLIO SUMMARY
============================================================
Stock           Quantity     Price        Total Value    
------------------------------------------------------------
AAPL            180          $150.50      $27,090.00     
TSLA            250          $220.75      $55,187.50     
------------------------------------------------------------
TOTAL PORTFOLIO VALUE:                    $82,277.50
============================================================
```

### Save Results (Optional)

```
Would you like to save the results? (yes/no): yes

Save portfolio data:
1. Text file (.txt)
2. CSV file (.csv)
3. Skip saving

Enter your choice (1-3): 1
Enter filename (without extension): my_portfolio
✓ Portfolio saved to my_portfolio.txt
```

## 🔑 Key Concepts

This project demonstrates essential Python programming concepts:

### 1. Dictionaries
```python
stocks = {"AAPL": 180, "TSLA": 250}
prices = {"AAPL": 150.50, "TSLA": 220.75}
```

### 2. Input/Output
```python
stock_name = input("Enter stock name: ").strip().upper()
print(f"✓ Added {quantity} shares of {stock_name}")
```

### 3. Basic Arithmetic
```python
stock_value = quantity * prices[stock]
total_value += stock_value
```

### 4. File Handling
```python
with open(filename, 'w') as f:
    f.write("Stock,Quantity,Price,Total Value\n")
```

### 5. Error Handling
```python
try:
    quantity = int(input(f"Enter quantity: "))
except ValueError:
    print("Invalid quantity. Please enter a number.")
```

### 6. Functions
```python
def calculate_portfolio_value(stocks, prices):
    # Modular, reusable code
    return total_value, portfolio_details
```

## 📊 Sample Output

### Text File Output (portfolio.txt)
```
STOCK PORTFOLIO TRACKER
============================================================

Stock           Quantity     Price        Total Value    
------------------------------------------------------------
AAPL            180          $150.50      $27,090.00     
TSLA            250          $220.75      $55,187.50     
------------------------------------------------------------
TOTAL PORTFOLIO VALUE: $82,277.50
```

### CSV File Output (portfolio.csv)
```
Stock,Quantity,Price,Total Value
AAPL,180,150.50,27090.00
TSLA,250,220.75,55187.50
TOTAL,,,82277.50
```


## 🎨 Customization

### Add More Stock Data
Modify the example data in the `main()` function:

```python
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 100,
    "MSFT": 150
}
```

### Change Output Format
Customize the table display in `calculate_portfolio_value()`:

```python
print(f"{'Stock':<20} {'Quantity':<15} {'Price':<15} {'Total':<15}")
```

### Add Currency Support
Modify the price input to support different currencies:

```python
currency = input("Enter currency symbol (default $): ") or "$"
print(f"{currency}{price:.2f}")
```

## 🚀 Future Enhancements

Ideas for extending this project:

- [ ] **Real-time price fetching** using APIs (yfinance, Alpha Vantage)
- [ ] **Historical data tracking** to see portfolio changes over time
- [ ] **Percentage calculations** (gains/losses, portfolio allocation)
- [ ] **Data visualization** with matplotlib or plotly
- [ ] **Database integration** (SQLite) for persistent storage
- [ ] **GUI interface** using Tkinter or PyQt
- [ ] **Multiple portfolio support** to track different accounts
- [ ] **Stock recommendations** based on portfolio analysis
- [ ] **Excel export** with formatting using openpyxl
- [ ] **Email notifications** for portfolio updates

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas
- Add input validation improvements
- Create unit tests
- Implement real-time stock price fetching
- Add data visualization features
- Improve error handling
- Write more comprehensive documentation

## 📝 Learning Outcomes

After completing this project, you will understand:

✅ How to use Python dictionaries for data storage  
✅ Input validation and error handling  
✅ File I/O operations (read/write)  
✅ String formatting and output presentation  
✅ Function organization and code modularity  
✅ Basic arithmetic and calculations  
✅ User interaction and menu systems  


## 👨‍💻 Author

Your Name
- GitHub: @yuvaakash1610 https://github.com/yourusername](https://github.com/yuvaakash1610
- LinkedIn: K YUVAAKASH https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/yuvaakash-kannan-450751360/


---

**Happy Tracking! 📈💰**

