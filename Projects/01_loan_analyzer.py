
import csv
from pathlib import Path


# ===============Automation of calculations for loan portfolio summaries.========================
# Loan costs list definition
loan_costs = [500, 600, 200, 1000, 450]

# Calculation and print of total number of loans in the list.
number_of_loans=len(loan_costs)
print("The total number of loans is:", number_of_loans)

# Calculation and print of the total of all loans in the list.
total_of_loans=sum(loan_costs)
print("The total of all loans is: $", total_of_loans)

# Calculation and print of the average loan price.
print(f"The average loan price is: ${int(total_of_loans/number_of_loans)}")


# =======Analysis of more detailed data on one of these loans to determine the investment evaluation========

# Loan dictionary definition
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extraction of "future value" and "remaining months" on the loan
future_value=loan.get("future_value")
remaining_months=loan.get("remaining_months")
print(f"Future value of the loan is: {future_value}")
print(f"Remaining months before the loan needs to be repaid: {remaining_months}")

# Calculation of "fair value" using Present Value.
discount_rate=0.20
present_value=(future_value)/(1+discount_rate/12)**remaining_months

# Decidion whether the present value of the loan is greater than or equal to the cost and hence worth to buy.
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")


# ============Financial calculations given the following new loan========================================
# New loan dictionary definition
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Definition of a new function that calculates present value.
def present_value_calculation(loan_info, annual_discount_rate):
    present_value=(loan_info.get("future_value"))/(1+annual_discount_rate/12)**loan_info.get("remaining_months")
    return present_value

# "Present value calculation" function call and print
present_value= present_value_calculation(new_loan,0.2)
print(f"The present value of the loan is: {present_value: .2f}")


# ============Selecting inexpensive loans from a list of loans===========================================
# List of dictionaries definition
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creation of the 'inexpensive_loans' list.
inexpensive_loans=[]

# Using loop through all the loans and adding those that cost $500 or less to the `inexpensive_loans` list.
for loan in loans:
    if loan.get("loan_price")<=500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)


# ================Saving the list of inexpensive loans to a csv file.======================================
# Setting the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Setting the output file path
output_path = Path("inexpensive_loans.csv")

# Using the csv library and 'csv.writer' writing the header and rows from the 'inexpensive_loans' list.
with open (output_path, 'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
