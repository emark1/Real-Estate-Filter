import os
import csv
from data_types import Purchase
import statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

def print_header():
    print('----------------')
    print('REAL ESTATE APP')
    print('----------------')
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'housingdata.csv')

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # print("Bed count: {}, type: {}".format(row['beds'], type(row['beds'])))
            p = Purchase.create_dict(row)
            purchases.append(p)
        return purchases 

        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(row)


# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#         print()

#         lines = []
#         for line in fin: 
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)

#         print(lines[:5])

# def get_price(p):
#     return p.price

def query_data(data):
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)
    high_purchase = data[-1]
    low_purchase = data[0]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds, low_purchase.baths))
    two_bedroom_homes = [
        p
        for p in data
        if p.beds == 2
    ]

    avg_price_2br = round(statistics.mean([p.price for p in two_bedroom_homes]))
    avg_baths_2br = round(statistics.mean([p.baths for p in two_bedroom_homes]))

    print("The average price of a 2br home is ${:,} and has {} bathrooms".format(avg_price_2br, avg_baths_2br))
    # for pur in data:
    #     prices.append(pur.price)
    # avg_price = statistics.mean(prices)
       # print("The average cost of a home is ${:,}".format(avg_price))


if __name__ == '__main__':
    main()