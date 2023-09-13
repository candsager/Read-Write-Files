import csv

cust_sales = open('sales.csv', 'r')
csv_file = csv.reader(cust_sales)
next(csv_file)

def main():
    outfile = open('salesreports.csv', 'w')
    outfile.write("Customer ID,Total\n")

    customerID = '250'
    total = 0

    for row in csv_file:
        sub_total = float(row[3])
        tax_amt = float(row[4])
        freight_amt = float(row[5])

        if customerID == row[0]:
            total += sub_total + tax_amt + freight_amt
        else:
            outfile.write(f"{customerID},{total:.2f}\n")
            customerID = row[0]
            total = sub_total + tax_amt + freight_amt

    outfile.write(f"{customerID},{total:.2f}\n")
    outfile.close()

main()
