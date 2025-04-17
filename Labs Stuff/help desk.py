#This work is a classmates As i missed class, i studied his system thoroughly, and took what i could to implment these concepts on my own.
# Ticket class simulates an IT support ticketing system
class Ticket:
    # Class-level variables for tracking overall ticket data
    ticket_id_counter = 1  # Used to assign unique ticket IDs
    stats = {'submitted': 0, 'resolved': 0, 'in_progress': 0, 'closed': 0}  # Tracks overall ticket status counts
    tickets = []  # Stores all created Ticket instances

    # Constructor method: initializes a new ticket instance
    def __init__(self, employee_id, name, issue):
        self.id = Ticket.ticket_id_counter  # Assign unique ticket ID
        Ticket.ticket_id_counter += 1  # Increment global ticket ID counter

        self.employee_id = employee_id  # Staff ID
        self.name = name  # Staff name
        self.issue = issue  # Description of the issue
        self.priority = self.set_priority()  # Set priority based on issue description
        self.status = "In Progress"  # Default status
        self.resolution = ""  # Empty resolution initially

        # Auto-resolve password reset issues
        if "password reset" in issue.lower():
            self.status = "Resolved"
            self.resolution = "Password reset. New pass: " + name[:2] + str(employee_id)[-2:]

        # Update statistics based on initial ticket status
        Ticket.stats['submitted'] += 1
        if self.status == "Resolved":
            Ticket.stats['resolved'] += 1
        else:
            Ticket.stats['in_progress'] += 1

        # Store the ticket instance in the class-level list
        Ticket.tickets.append(self)

    # Method to determine ticket priority based on issue type
    def set_priority(self):
        if "system outage" in self.issue.lower():
            return "High"
        elif "password reset" in self.issue.lower():
            return "Low"
        else:
            return "Medium"

    # Method for manager to approve and close high-priority in-progress tickets
    def manager_approve(self):
        if self.priority == "High" and self.status == "In Progress":
            self.status = "Closed"
            self.resolution = "Manager approved resolution."
            Ticket.stats['in_progress'] -= 1
            Ticket.stats['closed'] += 1

    # Method to display all ticket details
    def display(self):
        print("--------Info--------")
        print("")
        print("---------------------")
        print("Ticket ID:", self.id)
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Issue:", self.issue)
        print("Priority:", self.priority)
        print("Status:", self.status)
        print("Resolution:", self.resolution)
        print("-------------------")
        print("")

# Function to print current ticket statistics
def show_stats():
    print("--------Statistics--------")
    print("")
    print("---------------------")
    print("Tickets Submitted:", Ticket.stats['submitted'])
    print("Resolved:", Ticket.stats['resolved'])
    print("In Progress:", Ticket.stats['in_progress'])
    print("Closed:", Ticket.stats['closed'])
    print("---------------------")
    print("")

# Create sample tickets
t1 = Ticket(101, "Alice", "password reset")  # Auto-resolved
t2 = Ticket(102, "Bob", "system outage")     # High-priority, in-progress

# Manager approves the second ticket
t2.manager_approve()

# Display all ticket details
for t in Ticket.tickets:
    t.display()

# Show summary statistics
show_stats()
