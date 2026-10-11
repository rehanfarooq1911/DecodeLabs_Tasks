import math

def display_total(total):
    """Handles the DISPLAY (View) portion of the IPO model."""
    print("\n==============================")
    print("FINAL TOTAL: $", format(total, ",.2f"), sep="")
    print("==============================")

def main():
    total = 0.0          
    count = 0            

    print("DecodeLabs Expense Tracker Initialized.")
    print("Enter an expense amount (e.g., 100, 50, 20).")
    print("Type 'quit' to finish and see your total.\n")

    while True:
        raw = input("Enter expense (or 'quit'): ").strip()

        if raw.lower() == "quit":
            break

        try:
            new_expense = float(raw)
        except ValueError:
            print("Invalid Data. Please enter a number (e.g., 25 or 12.50).")
            continue

        if not math.isfinite(new_expense):
            print("Invalid Data. Please enter a real number.")
            continue

        if new_expense <= 0:
            print("Expense must be greater than zero.")
            continue

        total += new_expense
        count += 1
        
        print("Added $", format(new_expense, ",.2f"), " | Running total: $", format(total, ",.2f"), sep="")

    print("\nTransactions recorded:", count)
    print("FINAL TOTAL: $", format(total, ",.2f"), sep="")


if __name__ == "__main__":
    main()