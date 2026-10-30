from addProduct import add_product
from viewProduct import view_product
from testFunctions import test_entry

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

valid_types_results = ["PASS", "FAIL"]


def search_product():
    searchlist = []
    del searchlist[:]
    keyword = input("Enter keyword to search: ").lower()
    for p in database:
        if keyword in p["serial_number"].lower() or keyword in p["model"].lower() or any(keyword in test['technician'].lower() for test in p["tests"]) or any(keyword in test['testName'].lower() for test in p["tests"]):
            searchlist.append(p)
    
    if searchlist:
        return searchlist
    
    print("Product not found")
    return None


def quick_print(print_product):
    if print_product:
        for i in print_product:
            if print_product:
                print("Serial Number:", i['serial_number'])
                print("Model:", i['model'])
                print("Build Date:", i['build_date'])
                print("Status:", i['status'])
                print("Tests:")
                for test in i['tests']:
                    print("  Test Name:", test['testName'])
                    print("  Result:", test['result'])
                    print("  Technician:", test['technician'])
                    print("  Timestamp:", test['timestamp'])
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
        product_found = search_product()
        if product_found:
            print("Product found:", product_found)
            test_recorded = test_entry(valid_types_results)
            product_found[0]["tests"].append(test_recorded)
        else:
            print("Product not found.")
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
    