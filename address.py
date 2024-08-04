# address_entry.py

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

def display_address(address):
    print("\nAddress Details:")
    print(f"Street: {address['street']}")
    print(f"City: {address['city']}")
    print(f"State: {address['state']}")
    print(f"ZIP Code: {address['zip_code']}")

def main():
    address = get_address()
    display_address(address)
    
    # Optionally, you can save the address to a file
    with open('address.txt', 'w') as file:
        file.write(f"Street: {address['street']}\n")
        file.write(f"City: {address['city']}\n")
        file.write(f"State: {address['state']}\n")
        file.write(f"ZIP Code: {address['zip_code']}\n")
    
    print("\nAddress has been saved to 'address.txt'.")

if __name__ == "__main__":
    ma
