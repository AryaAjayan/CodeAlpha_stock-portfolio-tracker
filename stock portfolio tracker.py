import tkinter as tk
from tkinter import ttk, messagebox  # Import ttk for themed widgets
import random  # Using random to simulate stock data, remove for real API

class StockPortfolioTracker:
    def __init__(self, master):
        self.master = master
        master.title("Stock Portfolio Tracker")
        master.geometry("800x600")  # Adjust size as needed

        # Portfolio data (stock: quantity)
        self.portfolio = {}

        # Stock list (for demo purposes)
        self.stock_symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"] # Example stock symbols

        # UI elements
        self.create_widgets()

    def create_widgets(self):
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=5, relief="raised", font=('Arial', 10))
        style.configure("TLabel", padding=5, font=('Arial', 12))
        style.configure("TEntry", padding=5, font=('Arial', 12))
        style.configure("Treeview", font=('Arial', 10), rowheight=25)


        # Stock Symbol Input
        ttk.Label(self.master, text="Stock Symbol:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.stock_entry = ttk.Entry(self.master, width=10)
        self.stock_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Quantity Input
        ttk.Label(self.master, text="Quantity:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.quantity_entry = ttk.Entry(self.master, width=5)
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Add Stock Button
        add_button = ttk.Button(self.master, text="Add Stock", command=self.add_stock)
        add_button.grid(row=0, column=4, padx=5, pady=5)

        # Remove Stock Button
        remove_button = ttk.Button(self.master, text="Remove Stock", command=self.remove_stock)
        remove_button.grid(row=0, column=5, padx=5, pady=5)


        # Portfolio Treeview
        self.portfolio_tree = ttk.Treeview(self.master, columns=("Stock", "Quantity", "Price", "Value"), show="headings")
        self.portfolio_tree.heading("Stock", text="Stock")
        self.portfolio_tree.heading("Quantity", text="Quantity")
        self.portfolio_tree.heading("Price", text="Price")
        self.portfolio_tree.heading("Value", text="Value") # Added Value column
        self.portfolio_tree.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.master.grid_rowconfigure(1, weight=1) # Allow treeview to expand vertically
        self.master.grid_columnconfigure(0, weight=1) # Allow treeview to expand horizontally
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)
        self.master.grid_columnconfigure(4, weight=1)
        self.master.grid_columnconfigure(5, weight=1)


        #Total Value Label
        self.total_value_label = ttk.Label(self.master, text="Total Portfolio Value: $0.00")
        self.total_value_label.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky="w")
        # Refresh Button (Simulates updating prices)
        refresh_button = ttk.Button(self.master, text="Refresh Prices", command=self.update_prices)
        refresh_button.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

    def add_stock(self):
        stock = self.stock_entry.get().upper()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity.")
            return

        if stock not in self.stock_symbols: #Simple check to restrict the stock list
            messagebox.showerror("Error", "Stock not available")
            return

        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be positive.")
            return

        if stock in self.portfolio:
            self.portfolio[stock] += quantity
        else:
            self.portfolio[stock] = quantity
        self.update_portfolio_display()
        self.stock_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def remove_stock(self):
         stock = self.stock_entry.get().upper()
         try:
            quantity = int(self.quantity_entry.get())
         except ValueError:
            messagebox.showerror("Error", "Invalid quantity.")
            return

         if stock not in self.portfolio:
            messagebox.showerror("Error", "Stock not in portfolio.")
            return

         if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be positive.")
            return

         if quantity > self.portfolio[stock]:
            messagebox.showerror("Error", "Quantity exceeds holdings.")
            return

         self.portfolio[stock] -= quantity
         if self.portfolio[stock] == 0:
            del self.portfolio[stock]

         self.update_portfolio_display()
         self.stock_entry.delete(0, tk.END)
         self.quantity_entry.delete(0, tk.END)

    def get_stock_price(self, stock):
        # Replace this with an actual API call!
        # This is just a simulation
        return round(random.uniform(100, 200), 2)  # Simulate a price between 100 and 200

    def update_portfolio_display(self):
        # Clear the treeview
        for item in self.portfolio_tree.get_children():
            self.portfolio_tree.delete(item)

        total_value = 0
        for stock, quantity in self.portfolio.items():
            price = self.get_stock_price(stock)
            value = price * quantity
            total_value += value
            self.portfolio_tree.insert("", tk.END, values=(stock, quantity, price, value)) #Added 'Value' Column

        self.total_value_label.config(text=f"Total Portfolio Value: ${total_value:.2f}")

    def update_prices(self):
        self.update_portfolio_display()  # Just refresh the prices in the display

root = tk.Tk()
tracker = StockPortfolioTracker(root)
root.mainloop()