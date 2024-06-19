import csv
def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data
file_name = "data.csv"
data = read_csv_file(file_name)
print("Data from CSV file:")
for row in data:
    print(row)
