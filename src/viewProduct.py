def view_product(product):
    print("Product Details:")
    print(f"Serial Number: {product['serial_number']}")
    print(f"Model: {product['model']}")
    print(f"Build Date: {product['build_date']}")
    print(f"Status: {product['status']}")
    print("Tests:")
    for test in product["tests"]:
        print(f"  Test Name: {test['testName']}")
        print(f"  Result: {test['result']}")
        print(f"  Technician: {test['technician']}")
        print(f"  Timestamp: {test['timestamp']}")
        print()