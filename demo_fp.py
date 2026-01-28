# Traditional function to add an order (mutates global state)
orders = ['order1', 'order2']

# def add_order_traditional(new_order):
#     orders.append(new_order)

def add_order_fp(order_list,new_order):
    return order_list + [new_order]

# Usage
# add_order_traditional('order3')
orders = ['order1', 'order2']
new_orders = add_order_fp(orders, 'order3')
# orders remains unchanged; new_orders contains the added order
# orders is now ['order1', 'order2', 'order3']