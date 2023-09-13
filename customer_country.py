import csv

customers = open('customers.csv', 'r')
csv_file = csv.reader(customers)
next(csv_file)
def main():
# Read the file's contents.
    #file_contents = infile.read()
    outfile = open('customer_country.csv', 'w')

    outfile.write("Full name, Country \n")

    counter = 0

    for record in csv_file:
        fname = record[1]
        lname = record[2]
        cname = record[4]

        outfile.write(f"{fname} {lname} {cname}\n") 
        counter += 1            
        
    outfile.close()

    print(f"Total number of customers: {counter}")
# Call the main function.
main()