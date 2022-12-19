global products_dict, apple_discount, bread_discount
# initialize dictionary of products and prices
products_dict = {
    "soup": 0.65,
    "bread": 0.80,
    "milk": 1.30,
    "apples": 1.00
}
apple_discount = 0.1
bread_discount = 0.5


# preprocess data and get counts for each product
def get_products_count(input_str):
    products = input_str.strip().lower().split(' ')
    products_name = [x.lower() for x in products_dict]
    products_count = [products.count(x.lower()) for x in products_dict]
    products_count = dict(zip(products_name, products_count))
    return products_count


# calculate discount for special products
def calculate_discount(products_count, product1='apples', product2='bread', *args):
    calc_product1_discount, calc_product2_discount = 0, 0
    # discount for apples
    if products_count[product1] >= 1:
        product1_counter = products_count[product1]
        calc_product1_discount = apple_discount * products_dict[product1] * product1_counter if \
            product1_counter >= 1 else 0

    # discount for bread
    if products_count[product2] >= 1:
        product2_counter = products_count[product2]
        product2_discounts_number = products_count['soup'] // 2
        calc_product2_discount = bread_discount * products_dict[product2] * \
                                 (product2_discounts_number if product2_discounts_number < product2_counter else
                                  product2_counter) if product2_counter >= 1 else 0
    return calc_product1_discount, calc_product2_discount


# calculate subtotal and total prices
def calculate_prices(input_str):
    products_count = get_products_count(input_str)
    calc_discount1, calc_discount2 = calculate_discount(products_count)
    subtotal_price = sum([products_dict[x] * products_count[x] for x in products_count])
    total_price_discount = calc_discount1 + calc_discount2
    total_price = subtotal_price - total_price_discount
    return subtotal_price, total_price_discount, total_price, calc_discount1, calc_discount2


# print summary
def show_summary(subtotal_price, total_price_discount, total_price, calc_discount1, calc_discount2, *args):
    print(f'Subtotal: £{subtotal_price:0.2f} {"(No offers available)" if total_price_discount == 0 else ""}')
    if calc_discount1:
        print(f'Apples 10% off: £{calc_discount1:0.2f}')
    if calc_discount2:
        print(f'Bread 50% off: £{calc_discount2:0.2f}')
    print(f'Total: £{total_price:0.2f}')


print('Print a list of products')
input_ln = input()
subtotal, total_discount, total, calc_discount_apples, calc_discount_bread = calculate_prices(input_ln)
show_summary(subtotal, total_discount, total, calc_discount_apples, calc_discount_bread)
