from addProduct import add_product
from viewProduct import view_product

product = {
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
        }
    ]
}

while True: 
    print ("1. Add Product")
    print ("2. Record Test Result")
    print ("3. View Product History")
    print ("4. Search Products")
    print ("5. Technician Statistics")
    print ("6. Production Statistics")
    print ("7. Save Database")
    print ("8. Load Database")
    print ("9. Exit")
    menuChoice = input("Select an option: ")
    if menuChoice == "1":
        print("Add Product Selected")
        product = add_product()
    elif menuChoice == "2":
        print("x")
    elif menuChoice == "3":
        view_product(product)
    elif menuChoice == "4":
        print("x")
    elif menuChoice == "5":
        print("x")
    elif menuChoice == "6":
        print("x")
    elif menuChoice == "7":
        print("x")
    elif menuChoice == "8":
        print("x")
    elif menuChoice == "9":
        break
    else:
        print("Invalid option, please try again.")
    