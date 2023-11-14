#QQQ to NQ conversion algo
def qqq_to_nq(qqq_price):
    """
    Convert QQQ price to NQ value.
    1 NQ share is equivalent to ___ QQQ shares.
    """
    return qqq_price * 41.2113228

#NQ to QQQ conversion algo
def nq_to_qqq(nq_value):
    """
    Convert NQ value to QQQ price.
    1 NQ share is equivalent to ____ QQQ shares.
    """
    return nq_value / 41.2113228

#ES to SPY conversion algo
def es_to_spy(es_price):
    """
    Convert ES price to SPY value.
    1 ES share is equivalent to ___ SPY shares.
    """
    return es_price / 10.0508169


#SPY to ES conversion algo
def spy_to_es(spy_price):
    """
    Convert SPY value to ES price.
    1 ES share is equivalent to ___ SPY shares.
    """
    return spy_price * 10.0508169

# Main logic
conversion_type = input("Choose conversion (type 'QQQ to NQ', 'NQ to QQQ', 'ES to SPY', or 'SPY to ES'): ").strip().lower()

if conversion_type == "qqq to nq":
    qqq_price = float(input("Enter the current QQQ price: "))
    nq_value = qqq_to_nq(qqq_price)
    print(f"Equivalent NQ Value: {nq_value}")
elif conversion_type == "nq to qqq":
    nq_value = float(input("Enter the current NQ value: "))
    qqq_price = nq_to_qqq(nq_value)
    print(f"Equivalent QQQ Price: {qqq_price}")
elif conversion_type == "es to spy":
    es_price = float(input("Enter the current ES price: "))
    spy_value = es_to_spy(es_price)
    print(f"Equivalent SPY Value: {spy_value}")
elif conversion_type == "spy to es":
    spy_price = float(input("Enter the current SPY price: "))
    es_value = spy_to_es(spy_price)
    print(f"Equivalent ES Price: {es_value}")
else:
    print("Invalid conversion type. Please choose a valid option.")
