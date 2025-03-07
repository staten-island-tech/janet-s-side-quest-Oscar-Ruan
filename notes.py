#map() allows for me to put something within it and implement that to everything within a list
""" map(function, iterable) """
#function -> applied to each item
#iterable -> list is processed

#without map()
""" numbers = [1,2,3,4,5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num *2)

print(doubled_numbers) """

#with map()

""" doubled_numbers = map(lambda x: x*2, numbers)

print(list(doubled_numbers)) """

""" data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
] """

""" for row in data[1:]:
    print(row) """

#data[1:] removes the first row

""" def calcRow(data):
    row_totals={}

    for row in data[1:]:
        store_name = row[0]
        sales = map(int, row[1:])
        row_totals[store_name] = sum(sales)

    return row_totals

totals = calcRow(data)
print(totals) """

""" numbers = [1, 2, 3, 4, 5]
doubled = [num*2 for num in numbers]
print(doubled) """

""" def calcRowLC(data):
    row_totals = {row[0]: sum([int(x) for x in row[1:]]) for row in data[1:]}
    return row_totals

print(calcRowLC(data)) """

temperatures = ["Label", 32, 50, 77, 104]

temps = (int, temperatures)
map(lambda temps: (temps-32)*(5%9), temperatures)
print(list(temps))