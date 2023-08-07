def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY:   ")
    endDate = input("Please enter end date in the following format MM/DD/YYY:   ")
    return fromDate, endDate
 
def getEname():
    ename = input("Enter Employee Name: ")
    return ename

def getHoursWorked():
    hours = float(input("Enter Hours:   "))
    return hours


def getHourlyRate():
    hourlyrate = float(input("Enter Hourly Rate:    "))
    return hourlyrate

def getTaxRate():
    taxrate = float(input("Enter Tax Rate:  "))
    taxrate = taxrate / 100
    return taxrate

def CalcTaxAndNetPay(hours,hourlyrate,taxrate):
    gpay = hours * hourlyrate
    incometax = gpay * taxrate
    netpay = gpay - incometax
    return gpay, incometax, netpay

def printinfo(empDetailList):
    totalemployee = 0
    totalhours = 0.00
    totalgrosspay = 0.00
    totaltax = 0.00
    totalnetpay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate  = empList[1]
        ename = empList[2]
        hours = empList[3]
        hourlyrate = empList[4]
        taxrate = empList[5]

        gpay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromDate, endDate, ename,f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{gpay:,.2f}", f"{taxrate:,.1%}",
             f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalemployee += 1
        totalhours += hours
        totalgrosspay += gpay
        totaltax += incometax
        totalnetpay += netpay

        empTotals["totEmp"] = totalemployee
        empTotals["totHours"] = totalhours
        empTotals["totGross"] = totalgrosspay
        empTotals["totTax"] = totaltax
        empTotals["totNet"] = totalnetpay

def printTotals(empTotals):
    print(f"Total Number Of Employees:  {empTotals['totEmp']}")
    print(f"Total Hours of Employees:   {empTotals['totHours']}")
    print(f"Total Gross Pay of Employees: {empTotals['totGross']}")
    print(f"Total Tax of Employees: {empTotals['totTax']}")
    print(f"Total Net Pay of Employees: {empTotals['totNet']}")

if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        ename = getEname()
        if (ename.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyrate = getHourlyRate()
        taxrate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, ename)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyrate)
        empDetail.insert(5, taxrate)
        empDetailList.append(empDetail)
    printinfo(empDetailList)
    printTotals(empTotals)
        
