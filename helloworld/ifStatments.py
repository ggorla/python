is_good_credit = True
price = 1000000
if is_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: {down_payment}")