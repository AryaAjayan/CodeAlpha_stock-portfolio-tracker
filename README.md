This is a simple stock portfolio tracker application built with Python and Tkinter. It allows users to add, remove, and view their stock holdings. Please note that this application uses a simulated stock price API and is intended for demonstration purposes only. For real-world use, you will need to replace the simulated API with a connection to a real financial data provider.

## Features

*   **Add Stocks:** Add stock symbols and quantities to your portfolio.
*   **Remove Stocks:** Remove stocks and quantities from your portfolio.
*   **View Portfolio:** Display your current stock holdings, including stock symbol, quantity, price, and total value.
*   **Simulated Price Updates:** Simulate real-time stock price updates (replace with a real API for actual real-time data).
*   **Total Portfolio Value:** Calculates and displays the total value of your portfolio.

## Prerequisites

*   Python 3.x
*   Tkinter (usually comes with Python, but install separately if needed)

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [YOUR_REPOSITORY_URL]  # If you have a repository. Omit if you just have the python file.
    cd stock_portfolio_tracker # Change directory if needed
    ```

2.  **Install any necessary packages:**
    ```bash
    # Tkinter usually comes with python - you probably don't need this.
    # If you get an error like "ModuleNotFoundError: No module named 'tkinter'",
    # try one of these commands below:
    #
    #   On Debian/Ubuntu:
    # sudo apt-get install python3-tk
    #
    #   On MacOS:
    # brew install python-tk # If using brew
    #
    #   Using pip:
    # pip install tk
    ```
    *(It is *highly* unlikely that you will need to install `tkinter` separately, as it is part of the Python standard library)*.

## Usage

1.  **Run the application:**

    ```bash
    python stock_tracker.py
    ```

2.  **Interface Interaction:**
    *   Enter the stock symbol in the "Stock Symbol" field (e.g., AAPL, GOOG, MSFT, AMZN, TSLA - a limited list is checked in the demo version.)
    *   Enter the quantity in the "Quantity" field.
    *   Click "Add Stock" to add the stock to your portfolio.
    *   Click "Remove Stock" to remove stock from your portfolio.
    *   Click "Refresh Prices" to simulate updating the stock prices and portfolio value.

## Important Notes

*   **Simulated Stock Prices:** This application uses a *simulated* API for fetching stock prices. The prices are randomly generated and are not real-time.  To use this application with real stock data, you must replace the `get_stock_price` function with a call to a real financial data API.
*   **API Integration:** You will need to sign up for an account with a financial data provider (e.g., Alpha Vantage, IEX Cloud, Financial Modeling Prep) and obtain an API key. Consult the API provider's documentation for instructions on how to integrate their API into your Python code.
*   **Error Handling:** The current implementation includes basic error handling for quantity validation. You should add more robust error handling for API calls, invalid stock symbols, and other potential issues.
*   **Data Persistence:** The portfolio data is not currently saved when the application is closed. You can implement data persistence by saving the portfolio to a file (e.g., JSON) and loading it when the application starts.

## Code Structure

*   `stock_tracker.py`: Contains the main application code, including the UI and portfolio management logic.
