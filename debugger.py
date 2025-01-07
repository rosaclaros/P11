

def calculate_total(prices, tax_rate):
    total = 0
    for price in prices:
        total += price * (1 + tax_rate)
    return total

def main():
    prices = [10, 20, 30]
    tax_rate = 0.07  # 7% tax rate
    total = calculate_total(prices, tax_rate)
    print(f"Total with tax: {total}")

if __name__ == "__main__":
    main()

