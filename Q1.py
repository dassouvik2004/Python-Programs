def order_pizza(size, *toopings, **details):
    print(f'Ordered a {size} pizza with the following toopings: ')
    for topping in toopings:
        print(f'- {topping}')
    print('Details of the order are:')
    for key, value in details.items():
        print(f'- {key}: {value}')

order_pizza("large","Pepperoni","Olives",Total_Bill=1099,Delivary=True,Tip=5)