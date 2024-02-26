# input statements
salary = float(1250.0)
numDependents =2

# calculate taxes here

#find the the value of a virable named stateTax.
stateTax=(salary*6.5/100)

#find the value of a vairable named federalTax.
fedralTax=(salary*28.0/100)

#find the value of a vairable named depentetDeductation.
dependentDeducation=(salary*2.5/100)*numDependents

#find the value of a vairable named totalWithholding.
totalWithholding=stateTax + fedralTax + dependentDeducation

#find the a value of a vairable named takeHomePay.
takeHomePay= salary-totalWithholding

# output statements
#display each named vairable and it's value in seprate lines.
print("State Tax: $", str(stateTax))
print("Fedral Tax: $", str(fedralTax))
print("Dependents: $", str(dependentDeducation))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
