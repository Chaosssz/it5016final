#Gym_Member_info.py
#@auth ZJ 13.3.25 12:42pm
#step 1 collect gym member information

#using python input function, define function gym_member to contain these two inputs for info ammended to gym_member data
counter = 0

def gym_member():
    global counter
    date = input("Enter Today's Date: DD/MM/YYYY: ")
    name = input("Enter Your Name: ")
    membership_id = counter
    print(membership_id)
    print("Your Name is: ", name)
    print("You Signed up:", date)
    counter += 1
    return date, name, membership_id

#collect gym member info for 3 members
for membership_id in range(3):
    gym_member()
#new function, def membership_fee_total, to call membership ID, grab number, ask user to input membership type
# New function to calculate membership fee total
def membership_fee_total():
    # Call gym_member to get the user details
    date, name, membership_id = gym_member()
    print(f"Hello {name}, your Membership ID is {membership_id}.")

    # Ask user for number of add-ons
    add_ons_count = int(input("How Many Add-Ons? (1-8): "))
    add_item = {}

    # Collect add-on details
    for i in range(add_ons_count):
        add_on_name = input(f"Enter the Name of Add-On {i + 1}: ")
        amount = float(input(f"How Much $$ for {add_on_name}?: "))
        add_item[add_on_name] = amount

    # Calculate the total amount
    total = 0
    for k, v in add_item.items():
        total += v

    # Display the total
    print(f"Total Membership Fee (Including Add-Ons): ${total:.2f}")
    return total

# Call the `membership_fee_total` function
membership_fee_total()
#display total
#Gym member approval process function.
def gym_member_approval():
    date, name, m = gym_member_info()
    print(f"Hello {name}, your Membership ID is {membership_id}.")
    add_on=int(input("How Many Add-Ons? (1-8)"))

#calculate the total fee
total_fee = calculate_total_fee()
if total_fee < 1000:
    status = "Approved"
    approval_reference = f"{membership_id}-{membership_id[-3:]}" # member ID + last 3 chars
    print(f"Membership Approved! Status: {status}. Approval Reference: {approval_reference}.")
elif total_fee > 1000:
    status = "Pending"
    print(f"Membership Status: {status} (Total Fee Exceeds $1000.")
    print("Please contact the gym for further assistance.")
#return     the final status and approval4
else:
    "name", name,
    "membership_id", membership_id,
    "status", status,
    "total_fee", total_fee,
    "approval_reference", approval_reference if total_fee < 1000 else None


