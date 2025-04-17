#ClubMemberShip.py
#assessment part B: python class, generating statistic
#@auth ZJ 27/3/25 1:05
class ClubMembership:
    """Generate statistics"""
    counter = 10000
    total_registered = 0
    total_approved = 0
    total_pending = 0

    def __init__(self, name):
        """This is initializing all attributes for later referencing"""
        self.name = name
        self.mem_id = self.generate_id()
        self.add_on = {}
        self.total=300
        self.approval = ""
        ClubMembership.total_registered =+ 1

    def generate_id(self):
        ClubMembership.counter += 1 # increments by one
        return ClubMembership.counter

    def request_add_on(self):
        num = int(input("How many add ons do you require"))
        for i in range(num):
            add_on_name = input("Name Of Add-On: ")
            price = int(input("Enter The Price: "))
            self.add_on[add_on_name] = price
        self.total=sum(self.add_on.values())
        return self.total

    def add_on_approval(self):
        if self.total<=1000:
            self.approval="Approved"
            ClubMembership.total_approved += 1
        else:
            self.approval="Pending"
            ClubMembership.total_pending += 1 # this increments member to total.pending

    def display(self):
        print("Name: ", self.name)
        print("ID:  ", self.mem_id)
        print("Total:  ", self.total)
        print("Status:  ", self.approval)
        for add_on, price in self.add_on.items():
            print(add_on,":", price)

num_mem = int(input("How many members have registered today?"))
for i in range(num_mem):
    name = input("Enter Your Name: ")
    mem = ClubMembership(name)
    mem.request_add_on()
    mem.add_on_approval()
    mem.display()

print("Summary")
print("Total Registered: ", ClubMembership.total_registered)
print("Total Approved: ", ClubMembership.total_approved)
print("Total Pending: ", ClubMembership.total_pending)