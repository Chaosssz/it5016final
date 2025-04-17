# write a python function to capture the requesters name and project name for which the donation is needed
# Global counter for request ID's (outside of the function)
counter = 10000

# Function to generate_id(): denotes no params specified
def generate_id():
    global counter
    counter += 1 # increase global counter
    return counter

#function is SPECIFYING no parameters
# Function to capture, requesters name, proj_name, donation amount
def make_request(): #def funct make_req(): make_req: name = input proj_name = input amt = int(input("Donation Amount")
   name = input("Enter Your Name: ")
   proj_name = input("Enter Your Project Name: ")
   donation_amount = int(input("How much are you donating: $$?")) # what the fuck is this for?
   id = generate_id() #ID = generate ID, calls FUNCTION generate_id which ID = counter + 1
   return name, proj_name, donation_amount, id  #return name, proj_name, amt, ID


#enter items requested, name : price and then > calculate total.
def donation_details(): # function to gather donation details (item & price) and calculate the total.
    detail = {} # empty dictionary to store item details
    num = int(input("How many Items are you providing?:")) # gather total num of items (2)

    # Collect Item Details
    for i in range(num): #for loop to collect item details, item name, price, detail[item]
       item = input(f"Enter The Item Name{i + 1}: ")
       price = int(input(f"Enter The Price Of {item}: "))
       detail[item] = price # adds item:price to our empty dictionary
# Calculate total price of items
    total = 0
    for price in detail.values():
        total += price # add each items price to total
    #return details & total price
    return detail, total
def decision(name, proj_name, total, id): # function to make approval decisions based on conditions
    # initialize priority, status, and approval_id (AS STRINGS "" NOT () TUPLES )
    priority = ""
    status = ""
    approval_id = ""
    #decison based on proj_name & total donation amount
    if "Family" in proj_name:
        priority = "High"
        status = "Approved"
        approval_id = str(id) + name[-2:] # request ID + last 2 chars of name
    elif total < 500: # if the requested total is less than 500, set prio to medium & approval_status to "Approved" automatically
        priority = "Medium"
        status = "Approved"
        approval_id = str(id) + name[2:]
    else:
        priority = "Low"
        status = "Pending"

    return priority, status, approval_id

# Function to display the final output
def display_request():
    # Task 1: Capture req details
    name, proj_name, donation_amount, id = make_request()
    # Task 2 : capture donation item details & calculate total
    detail, total = donation_details()
    # Task 3: Make approval decisions
    priority, status, approval_id = decision(name, proj_name, total, id)
    # Task 4 : Display all outputs
    print("\n--- Donation Request Summary ---")
    print(f"Requester Name: {name}")
    print(f"Project Name: {proj_name}")
    print(f"Request ID: {id}")
    print(f"Requested Items: {detail}")
    print(f"Total Requested Amount: ${total}")
    print(f"Priority: {priority}")
    print(f"Status: {status}")
    if approval_id:
        print(f"Approval ID: {approval_id}")
# Main Program
display_request()