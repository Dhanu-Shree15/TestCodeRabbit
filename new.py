def get_address():
    print("Please enter your address details.")
    
    street = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP Code: ")
    
    # Store or process the address here
    address = {
        "street": street,
        "city": city,
        "state": state,
        "zip_code": zip_code
    }
    
    return address