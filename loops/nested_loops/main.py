produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for i in groceries[0]:
    for x in groceries[1]:
        print(f"Item name: {i} {x}")