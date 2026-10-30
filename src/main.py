from addProduct import add_product
from viewProduct import view_product

database = [
    {
    "serial_number": "SN1001",
    "model": "X100",
    "build_date": "2026-10-30",
    "status": "In Progress",

    "tests": [
        {
            "testName": "Electrical Test",
            "result": "PASS",
            "technician": "Sam",
            "timestamp": "2026-10-30 09:15"
        }]
    }
]



def search_product():
   serial_number = input("Enter serial number to search: ")
   for p in database:
      if p["serial_number"].lower() == serial_number.lower():
         product_found = p
         return product_found
      
   print("Product not found")
   return None

def quick_print(print_product):
    if print_product:
        print("Serial Number:", print_product["serial_number"])
        print("Model:", print_product["model"])
        print("Build Date:", print_product["build_date"])
        print("Status:", print_product["status"])
        print("Tests:")
        for test in print_product["tests"]:
            print("  Test Name:", test["testName"])
            print("  Result:", test["result"])
            print("  Technician:", test["technician"])
            print("  Timestamp:", test["timestamp"])
    else:
        print("No product to display.")


while True: 
    print ("1. Add Product")
    print ("2. Record Test Result")
    print ("3. View Product History")
    print ("4. Search Products")
    print ("5. Technician Statistics")
    print ("6. Production Statistics")
    print ("7. Save Database")
    print ("8. Load Database")
    print ("9. Sam stuff")
    menuChoice = input("Select an option: ")
    if menuChoice == "1":
        database.append(add_product())
    elif menuChoice == "2":
        print("x")
    elif menuChoice == "3":
        view_product(database)
    elif menuChoice == "4":
        product_found = search_product()
        quick_print(product_found)
    elif menuChoice == "5":
        print("x")
    elif menuChoice == "6":
        print("x")
    elif menuChoice == "7":
        print("x")
    elif menuChoice == "8":
        print("x")
    elif menuChoice == "9":
        print(database)
 #       break
    else:
        print("Invalid option, please try again.")
    