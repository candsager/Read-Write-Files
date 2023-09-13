import csv

def main():


    employee_bon = open('employeePay.csv', 'r')

    csv_file = csv.reader(employee_bon)

    next(csv_file)


    for csv_file in csv_file:
        sal_bon = int(csv_file[3])
        bon_per = float(csv_file[4])
        bonus = sal_bon * bon_per
        total_pay = sal_bon + bonus 
        print(f'First Name: {csv_file[1]}')
        print(f'Last Name: {csv_file[2]}')
        print(f'Salary: ${sal_bon: 10,.2f}')
        print(f'Bonus: ${bonus: 10,.2f}')
        print(f'Pay: ${total_pay: 10,.2f}')
        input()

main()