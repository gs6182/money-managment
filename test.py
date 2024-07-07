import csv

# Read the data from the CSV file
with open('feb.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Sort the data by category
sorted_data = sorted(data, key=lambda x: x['Category'])

# Initialize variables for storing the total amounts
transportation_total = 0
groceries_total = 0
dining_out_total = 0
entertainment_total = 0
shopping_total = 0

# Loop through the sorted data and calculate the totals for each category
for item in sorted_data:
    amount = float(item['Amount'])
    category = item['Category']
    
    if category == 'Transportation':
        transportation_total += amount
    elif category == 'Groceries':
        groceries_total += amount
    elif category == 'Dining Out':
        dining_out_total += amount
    elif category == 'Entertainment':
        entertainment_total += amount
    elif category == 'Shopping':
        shopping_total += amount

# Print the total amounts for each category
print('Transportation Total: $', transportation_total)
print('Groceries Total: $', groceries_total)
print('Dining Out Total: $', dining_out_total)
print('Entertainment Total: $', entertainment_total)
print('Shopping Total: $', shopping_total)
