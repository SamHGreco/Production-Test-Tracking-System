
def add_product():
    serial_number = input("Enter serial number: ")
    model = input("Enter model: ")
    build_date = input("Enter build date (YYYY-MM-DD): ")
    status = "New"

    return {
        "serial_number": serial_number,
        "model": model,
        "build_date": build_date,
        "status": status,
        "tests": []
    }
