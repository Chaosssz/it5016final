#requsitionsystem.py # software developoment assessment part B
#@auth ZJ 11/4/25 11:11am
#Testing Completed 8.24pm

class RequisitionSystem: # define class RequisitionSystem to manage all Requisition Operations
    """
      Methods:
      @classmethod to call & increment counter to avoid putting outside of class.
      A dictionary to track number of requisitions by status.
      A list to store all submitted requisition objects.
    """
    stats = {'Pending':0, 'Submitted':0,'Approved':0,'Not Approved':0}
    all_requisitions = []
    #Class level counter for requisition ID's
    _counter = 00

# Constructor method - Called each time a new requisition is made.
    def __init__(self):
        """Initialize a new requistion with default values"""
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"
        self.requisition_id = RequisitionSystem.generate_requisition_id()

    #Class Counter
    @classmethod
    def generate_requisition_id(cls):
        """Generates a unique requisition ID, Increment, Return"""
        current = cls._counter # added this so it increments correctly was showing 6 prior because i messed up order
        cls._counter += 1
        return current

    def staff_info(self):
        """Collects Basic staff info"""
        self.date = input("Enter Today's Date (DD/MM/YY): ")
        self.staff_id = input("Enter Staff ID (e.g, FN21): ")
        self.staff_name = input("Enter Staff Name: ")

    def requisitions_details(self):
        """Accepts item names and costs, calculates total, and updates submitted stats."""
        num_items = int(input("\nHow many items are you requesting?: "))
        items = {} #dictionary for items inputted
        for _ in range(num_items):
            name = input("Enter Item Name: ")
            cost = float(input(f"Enter price of {name} ($): "))
            items[name] = cost


        self.total = sum(items.values())
        self.status = "Submitted"
        RequisitionSystem.stats['Submitted'] += 1


    def requisitions_approval(self):
        """Applies approval logic based on the Total cost of requisition items"""
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            RequisitionSystem.stats['Approved'] += 1 # appends +1 to stats
        else:
            self.status = "Pending"
            RequisitionSystem.stats['Pending'] += 1

        print("\nRequisition Successfully submitted!")  # Prints individual requisitions to help test entries
        self.display_requisition()  #
        RequisitionSystem.all_requisitions.append(self)  # Appends requisition info as it's added

    def requisitions_response(self, response):
        """Manager responds to pending requisition, to approve or reject"""
        if self.status == "Pending":
            RequisitionSystem.stats['Pending'] -= 1
            if response.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
                RequisitionSystem.stats['Approved'] += 1
            elif response.lower() == "not approved":
                self.status = "Not Approved"
                self.approval_reference = "Not available"
                RequisitionSystem.stats['Not Approved'] += 1

    def display_requisition(self):
        """Prints requisition information in required format."""
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")

    @classmethod
    def requisition_statistics(cls):
        """
        Displays requisition statistic summary
        Formatted for readability.
        """
        print("\n--- Requisition Statistics ---")
        print(f"Total Submitted: {cls.stats['Submitted']}")
        print(f"Total Approved: {cls.stats['Approved']}")
        print(f"Total Pending: {cls.stats['Pending']}")
        print(f"Total Not Approved: {cls.stats['Not Approved']}")

if __name__ == "__main__": #Only run the following code when this file is executed directly.
    print("\n--- Submit 5 Requisitions ---\n")
    """Method To allow testing of 5 entries and manager approval"""
    for i in range(5):
        print(f"\n--- Requisition {i+1} ---")
        req = RequisitionSystem()
        req.staff_info()
        req.requisitions_details()
        req.requisitions_approval()

    # View Statistics after 5 entries
    RequisitionSystem.requisition_statistics()

    # Let Manager respond to pending requests
    print("\n--- Manager Responds to Pending Requisitions ---\n")
    for req in RequisitionSystem.all_requisitions:
        if req.status == "Pending":
            print(f"\nPending Requisition ID: {req.requisition_id}")
            print(f"Submitted by {req.staff_name} on {req.date}")
            decision = input("Enter manager decision (Approved / Not Approved): ")
            req.requisitions_response(decision)

    # Final display of it all
    print("\n--- Final Requisition Summary ---")
    for req in RequisitionSystem.all_requisitions:
        req.display_requisition()

    # Final statistics
    RequisitionSystem.requisition_statistics()
