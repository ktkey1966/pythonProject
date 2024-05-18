#Kevin Key Phase 3 Project
#5/17/2024

def GetEmpName():
    empName = input('Enter employee name: ')
    return empName

def GetDatesWorked():
    fromDate = input('Enter Start Date (mm/dd/yyyy): ')
    toDate = input('Enter End Date (mm/dd/yyyy): ')
    return fromDate, toDate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    hourlyRate = float(input('Enter hourly rate: '))
    return hourlyRate

def GetTaxRate():
    taxRate = float(input('Enter tax rate: '))
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printInfo(EmpDetailList):
    totEmployees = 0
    totHours = 0.00
    totGrossPay = 0.00
    totTax = 0.00
    totNetPay = 0.00

    for EmpList in EmpDetailList:
        fromDate = EmpList[0]
        toDate = EmpList[1]
        empName = EmpList[2]
        hours = EmpList[3]
        hourlyRate = EmpList[4]
        taxRate = EmpList[5]

        grossPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, toDate, empName, f'{hours:,.2f}', f'{hourlyRate:,.2f}', f'{grossPay:,.2f}', f'{taxRate:,.1%}',
              f'{incomeTax:,.2f}', f'{netPay:,.2f}')

        totEmployees += 1
        totHours += hours
        totGrossPay += grossPay
        totTax += incomeTax
        totNetPay += netPay

        EmpTotals['totEmp'] = totEmployees
        EmpTotals['totHrs'] = totHours
        EmpTotals['totGrossPay'] = totGrossPay
        EmpTotals['totTax'] = totTax
        EmpTotals['totNetPay'] = totNetPay

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["totEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["totHrs"]}')
    print(f'Total Gross Pay: {EmpTotals["totGrossPay"]}')
    print(f'Total Income Tax: {EmpTotals["totTax"]}')
    print(f'Total Net Pay: {EmpTotals["totNetPay"]}')

def WriteEmployeeInformation(employee):
    file = open('employeeinfo.txt', 'a')

    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))


def GetFromDate():
    valid = False
    fromDate = ''

    while not valid:
        fromDate = input('Enter From Date (mm/dd/yyyy): ')
        if(len(fromDate.split('/')) != 3 and fromDate.upper() != 'ALL'):
            print('Invalid Date Format: ')
        else:
            valid = True

    return fromDate

def ReadEmployeeInformation(fromDate):
    EmpDetailList = []
    file = open('employeeinfo.txt', 'r')
    data = file.readlines()

    condition = True
    if fromDate.upper() == 'ALL':
        condition = False

    for employee in data:
        employee = [x.strip() for x in employee.strip().split('|')]
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2],
                                  float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromDate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2],
                                      float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList

if __name__ == '__main__':
    EmpDetailList = []
    EmpTotals = {}

    while True:
        empName = GetEmpName()
        if(empName.upper() == 'END'):
            break

        fromDate, toDate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyRate = GetHourlyRate()
        taxRate = GetTaxRate()

        print()
        EmpDetail = [fromDate,toDate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(EmpDetail)

    print()
    print()
    fromDate = GetFromDate()

    EmpDetailList = ReadEmployeeInformation(fromDate)
    print()
    printInfo(EmpDetailList)



