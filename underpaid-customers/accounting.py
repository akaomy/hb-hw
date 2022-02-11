melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00


''' Checks if expected payment is equal to the amoun paid '''
def check_payment_discrepancies(melon_cost, customer_name, melons_bought, customer_paid):
    expected = melons_bought * melon_cost
    if expected != customer_paid:
        print(f"{customer_name} paid ${customer_paid:.2f},", f"expected ${expected:.2f}")
    else:
        print(f'{customer_name} paid for product in full')

check_payment_discrepancies(melon_cost, customer1_name, customer1_melons, customer1_paid)
check_payment_discrepancies(melon_cost, customer2_name, customer2_melons, customer2_paid)
check_payment_discrepancies(melon_cost, customer3_name, customer3_melons, customer3_paid)
check_payment_discrepancies(melon_cost, customer4_name, customer4_melons, customer4_paid)
check_payment_discrepancies(melon_cost, customer5_name, customer5_melons, customer5_paid)
check_payment_discrepancies(melon_cost, customer6_name, customer6_melons, customer6_paid)
