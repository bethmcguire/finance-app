# author: Beth McGuire
# class: CSc 110
# description: application used for budgeting purposes. Takes in annual salary 
# and monthly expenses to help figure out financials

import os

print('-----------------------------')
print("----- WHERE'S THE MONEY -----")
print('-----------------------------')

annual_salary = input('What is your annual salary?\n')

if annual_salary.isnumeric():
    annual_salary = int(annual_salary)
else:
    print('Must enter positive integer for salary.')
    os._exit(0)

mortgage = input('How much is your monthly mortgage or rent?\n')

if mortgage.isnumeric():
    mortgage = int(mortgage)
else:
    print('Must enter positive integer for mortgage or rent.')
    os._exit(0)

bills = input('What do you spend on bills monthly?\n')

if bills.isnumeric():
    bills = int(bills)
else:
    print('Must enter positive integer for bills.')
    os._exit(0)

groceries = input('What are your weekly grocery/food expenses?\n')

if groceries.isnumeric():
    groceries = int(groceries)
else:
    print('Must enter positive integer for food.')
    os._exit(0)

travel = input('How much do you spend on travel annually?\n')

if travel.isnumeric():
    travel = int(travel)
else:
    print('Must enter positive integer for travel.')
    os._exit(0)

tax_percentage = ''

if annual_salary >= 0 and annual_salary <= 15000:
    tax_percentage = 10
elif annual_salary > 15000 and annual_salary <= 75000:
    tax_percentage = 20
elif annual_salary > 75000 and annual_salary <= 200000:
    tax_percentage = 25
else:
    tax_percentage = 30

after_taxes = annual_salary * (tax_percentage / 100)

if after_taxes >= 75000:
    after_taxes = 75000

extra = annual_salary - ((mortgage*12) + (bills * 12) + (groceries *52) + travel + after_taxes)
dash = '-'*(42)
print()
if mortgage*12 >= bills*12 and mortgage*12 >= groceries*52 and mortgage*12 >= travel and mortgage*12 >= extra:
    print(dash + '-' * int(round(((mortgage*12)/annual_salary)*100, 1)))
elif bills*12 >= mortgage*12 and bills*12 >= groceries*52 and bills*12 >= travel and bills*12 >= extra:
    print(dash + '-' * int(round(((bills*12)/annual_salary)*100, 1)))
elif groceries*52 >= mortgage*12 and groceries*52 >= bills*12 and groceries*52 >= travel and groceries*52 >= extra:
    print(dash + '-' * int(round(((groceries*52)/annual_salary)*100,1)))
elif travel >= mortgage*12 and travel >= bills*12 and travel >= groceries*52 and travel >= extra:
    print(dash + '-' * int(round((travel/annual_salary)*100, 1)))
elif extra >= mortgage*12 and extra >= bills*12 and extra >= groceries*52 and extra >= travel:
    print(dash + '-' * int(round((extra/annual_salary)*100,1)))
print('See the financial breakdown below, based on a salary of $' + str(annual_salary,))
if mortgage*12 >= bills*12 and mortgage*12 >= groceries*52 and mortgage*12 >= travel and mortgage*12 >= extra:
    print(dash + '-' * int(round(((mortgage*12)/annual_salary)*100, 1)))
elif bills*12 >= mortgage*12 and bills*12 >= groceries*52 and bills*12 >= travel and bills*12 >= extra:
    print(dash + '-' * int(round(((bills*12)/annual_salary)*100, 1)))
elif groceries*52 >= mortgage*12 and groceries*52 >= bills*12 and groceries*52 >= travel and groceries*52 >= extra:
    print(dash + '-' * int(round(((groceries*52)/annual_salary)*100,1)))
elif travel >= mortgage*12 and travel >= bills*12 and travel >= groceries*52 and travel >= extra:
    print(dash + '-' * int(round((travel/annual_salary)*100, 1)))
elif extra >= mortgage*12 and extra >= bills*12 and extra >= groceries*52 and extra >= travel:
    print(dash + '-' * int(round((extra/annual_salary)*100,1)))

print('| mortgage/rent | $ ' + format((mortgage * 12), '10,.2f') + ' |  '+ 
format(((mortgage * 12)/annual_salary)*100, '4,.1f') + '% ' + '| ' + '#' * 
int(round(((mortgage * 12)/annual_salary)*100, 1)))
print('|         bills | $ ' + format(bills * 12, '10,.2f') + ' |  ' + 
format(((bills * 12)/ annual_salary)*100, '4,.1f') + '%' + ' | ' + '#' * 
int(round(((bills * 12)/annual_salary)*100, 1)))
print('|          food | $ ' + format(groceries * 52, '10,.2f') + ' |  ' + 
format(((groceries * 52)/annual_salary)*100, '4,.1f') + '%' + ' | ' + '#' * 
int(round(((groceries * 52)/annual_salary)*100, 1)))
print('|        travel | $ ' + format(travel, '10,.2f') + ' |  ' +  
format((travel/annual_salary)*100, '4,.1f') + '%' + ' | ' + '#' * 
int(round((travel/annual_salary)*100, 1)))
print('|           tax | $ '  + format(after_taxes, '10,.2f')  + ' |  ' + 
format((after_taxes/annual_salary)*100, '4,.1f') + '%' + ' | ' + '#' * 
int(round((after_taxes/annual_salary)*100,1)))
print('|         extra | $ ' + format(extra, '10,.2f') + ' |  ' + 
format((extra/annual_salary)*100, '4,.1f') + '%' + ' | ' + '#' * 
int(round((extra/annual_salary)*100,1)))

if (mortgage*12) >= (bills*12) and (mortgage*12) >= (groceries*52) and (mortgage*12) >= travel and (mortgage*12) >= extra:
    print(dash + '-' * int(round(((mortgage*12)/annual_salary)*100, 1)))
elif (bills*12) >= (mortgage*12) and (bills*12) >= (groceries*52) and (bills*12) >= travel and (bills*12) >= extra:
    print(dash + '-' * int(round(((bills*12)/annual_salary)*100, 1)))
elif (groceries*52) >= (mortgage*12) and (groceries*52) >= (bills*12) and (groceries*52) >= travel and (groceries*52) >= extra:
    print(dash + '-' * int(round(((groceries*52)/annual_salary)*100,1)))
elif travel >= (mortgage*12) and travel >= (bills*12) and travel >= (groceries*52) and travel >= extra:
    print(dash + '-' * int(round((travel/annual_salary)*100, 1)))
elif extra >= (mortgage*12) and extra >= (bills*12) and extra >= (groceries*52) and extra >= travel:
    print(dash + '-' * int(round((extra/annual_salary)*100,1)))

if tax_percentage == 30 :
    print('>>> TAX LIMIT REACHED <<<')

if extra < 0:
    print('>>> WARNING: DEFICIT <<<')