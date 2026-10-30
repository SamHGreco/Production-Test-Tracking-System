from datetime import datetime


def test_entry(validtypes):

    test_name = input("Enter test name: ")
    while True: 
        result = input("Enter test result: ").upper()
        if result not in validtypes:
            print("Invalid result. Please enter PASS or FAIL.")
        else:
            break

    technician = input("Enter technician name: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    return {
        "testName": test_name,
        "result": result,
        "technician": technician,
        "timestamp": timestamp
    }