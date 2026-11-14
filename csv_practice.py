import csv

# Exercise 2: Read and print raw rows
print("Exercise 2")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3: Skip the header
print("\nExercise 3")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("\nExercise 4")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue = total_revenue + total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write
print("\nExercise 5")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count = original_count + 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_count = cleaned_count + 1

print("Original rows:", original_count)
print("Cleaned rows:", cleaned_count)

# Exercise 6: csv.DictReader
print("\nExercise 6")

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue = dict_total_revenue + total

        print(f"{product}: ${total:.2f}")

print(f"Total Revenue: ${dict_total_revenue:.2f}")

# csv.reader is useful when I want to access data by its position.
# DictReader is better when I want to access data using column names.

# Exercise 7: Sales summary by product
print("\nExercise 7")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] = sales_summary[product] + total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# Exercise 8: Append mode log
print("\nExercise 8")

from datetime import datetime

now = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{now} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated")