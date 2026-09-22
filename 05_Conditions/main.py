def process(user, order):
    if user:
        if user.active:
            if order:
                if order.status == "pending":
                    print("Processing Order")
                else:
                    print("Order already processed")
            else:
                print("No order found")
        else:
            print("User is not active")
    else:   
        print("No user found")



# Guard Clauses
def process(user, order):
    if not user:
        print("No user found")
        return
    if not user.active:
        print("User is not active")
        return
    if not order:
        print("No order found")
        return
    if order.status != "pending":
        print("Order already processed")
        return

    print("Processing Order")




def calculate_discount(user, cart):
    if user is not None:
        if user.is_premium:
            if len(cart) > 0:
                if cart.total > 500:
                    return cart.total * 0.20   # 20% off
                else:
                    return cart.total * 0.10   # 10% off
            else:
                return 0
        else:
            return 0
    else:
        return 0
    

def calculate_discount(user, cart):
    if user is None:         return 0    # Guard 1: no user
    if not user.is_premium:  return 0    # Guard 2: not premium
    if len(cart) == 0:       return 0    # Guard 3: empty cart
    # All guards passed — now compute the actual discount
    if cart.total > 500:
        return cart.total * 0.20   # 20% off
    return cart.total * 0.10   # 10% off
