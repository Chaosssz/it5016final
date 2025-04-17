#task1: create a python function called staff_info, use python input methods to collect information
#@auth ZJ 20/3/25 12:42pm fin 10:18pm

# Global counter id starts at (10000)
counter = 10000
# Function - Generate req ID
def generate_requisition_id():
    """generates and returns requisition id by incrementing global counter"""
    global counter
    counter += 1 # Increments counter by 1
    return counter # Return req ID +1

# Task 1 - (staff_info)

def staff_info():
    """Collects staff information and returns date, staff ID, staff name, and requisition ID."""
    date = input("Please Enter Today's Date: DD/MM/YYYY: ")
    staff_id = input("Please Enter Staff's ID (e.g., FN19): ")
    staff_name = input("Please Enter Staff's Name: ")
    requisition_id = generate_requisition_id()
    return date, staff_id, staff_name, requisition_id


# Task 2 - (requisition_total)
def requisition_total(): # call staff_info from task - 1
    """Calls staff_info(), collects item detail and returns total amount """
    # GET STAFF INFO ONCE
    date, staff_id, staff_name, requisition_id = staff_info()

    print("\n--- Printing Staff Information! ---")
    print(f"Date: {date}")
    print(f"Staff's ID: {staff_id}")
    print(f"Staff's Name: {staff_name}")
    print(f"Requisition ID: {requisition_id}")

    # Get number of items for requisition
    numb_item = int(input("\nHow Many Items are you requesting?: "))
    # Dictionary to store item_name : price
    items = {}

    # Collect item details
    for i in range(numb_item):
        item_name = input(f"Please Enter Item Name: ")
        item_price = float(input(f"Enter Price of {item_name} ($): "))
        items[item_name] = item_price


    # Calc total price
    total = sum(items.values())

    # returns total listed items and calculated items.values
    return total, staff_id, requisition_id, date, staff_name

# Task 3 - Requisition approval logic
def requisition_approval():
    """
    Approves or sets requisition status based on the total
    Returns:
        total, status, approval_reference, staff_id, requisition_id, date and staff_name
     """
    total, staff_id, requisition_id, date, staff_name = requisition_total()
    status = "Pending" # Default Status
    approval_reference = None

    # Approval logic
    if total < 500:
        status = "Approved"
        # Get last 3 chars of req ID (Padded with 00's if needed)
        req_id_str = str(requisition_id).zfill(5) # e.g, (10001)
        approval_reference = staff_id + req_id_str[-3:]


#always return values even if not approved
    return total, status, approval_reference, staff_id, requisition_id, date, staff_name

# Task 4 - Display Requisition
def display_requisitions():
    """
    Displays all the staff's basic information and the total value of his requisition
    """
# unpack all 7 values returned by requisition_approval()
total, status, approval_reference, staff_id, requisition_id, date, staff_name = requisition_approval()

# Display Requisition Details
print("\n--- Printing Requisition Information! ---")
print(f"Date: {date}")
print(f"Requisition ID: {requisition_id}")
print(f"Staff's ID: {staff_id}")
print(f"Staff's Name: {staff_name}")
print(f"Total : ${total}")
print(f"Status: {status}")
if approval_reference:
    print(f"Approval Reference Number: {approval_reference}")

# run the display function
display_requisitions()