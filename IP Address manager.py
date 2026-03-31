#Clean Format of IP Manager System.
import ipaddress
file_Name = "ips.txt"
# Function To read IP files....
def read_ip():
    try:
        with open(file_Name, "r") as file:
            return [line.strip() for line in file]
    
    except FileNotFoundError:
        return []

# Writing IP Addressess
def write_ips(ips):
    with open(file_Name, "w") as file:
        for ip in ips:
            file.write(ip + "\n")

# Adding Ip Addresses
def add_ip():
    try:
        ip = input("Enter IP Address:")
        ip  = str(ipaddress.ip_address(ip))
        
        ips  = read_ip()
        
        if ip in ips:
            print("IP address already exist")
            return
        
        ips.append(ip)
        write_ips(ips)
        
        print("IP address added successfully")
        
    except ValueError:
        print("Invalid IP address.")
        
# Viewing  for IP Addressess
def view_ip():
    ips = read_ip()
    
    if not ips:
        print("No IPs saved yet")
        return
    
    print("\nSaved IP Addresses")
    for ip in ips:
        print(ip)

# Searching for IP address
def search_ip():
    try:
        ip = str(ipaddress.ip_address(input("Enter IP address:")))
    except ValueError:
        print("Invalid IP Address!")
        return
    
    ips  = read_ip()
    
    if ip in ips:
        print("IP found!")
    else:
        print("IP not found!")

# Deleting ip address
def delete_ip():
    try:
        ip = str(ipaddress.ip_address(input("Enter IP address:")))
    except ValueError:
        print("Invalid IP Address!")
        return
    
    ips = read_ip()
    
    if ip not in ips:
        print(f"IP '{ip}' not found!")
        return

    ips.remove(ip)
    write_ips(ips)
    
    print(f"IP '{ip}' deleted successfully")

# The Terminal Menu
def menu():
    while True:
        print("\n====IP MANAGER=====")
        print("1.Add IP Address")
        print("2.View IP Address")
        print("3.Search IP Address")
        print("4.Delete IP Address")
        print("5.Exit")
        
        try:
            choice = int(input("Option number:"))
        except ValueError:
            print("Enter a valid number!")
            continue
        
        if choice == 1:
            add_ip()
        elif choice == 2:
            view_ip()
        elif choice == 3:
            search_ip()
        elif choice == 4:
            delete_ip()
        elif choice == 5:
            print("Goodbye....")
            break
        else:
            print("Invalid choice!")
menu()