IT5016_A3_20241486
Introduction
This document outlines my work for Assessment 3, which involved researching and applying programming principles and concepts to create a software repository. My main focus has been the Requisition Management System, a Python-based application that simulates a real-world requisition workflow using object-oriented techniques.

This system allows users to submit requisition requests, automatically evaluates approval status based on cost, and allows for manager reviews. In addition to this project, I have included several practical code exercises developed throughout the course in a folder titled labs. Each file in the repository has been commented and structured to demonstrate my understanding of Python class design, logic flow, and software design principles.
(aside from 1)

Project Overview: Requisition System
The requisition system was built utilizing core object oriented programming features in Python. It uses class-based structure to handle the full life cycle of our requisition, from submission to final approval, whilst also tracking overall statistics & activity along the way.
Key features include:
Unique requisition ID generation.
Staff detail collection & storage 
Itemized requisition entry with cost input
Approval logic – based on overall cost threshold
Manager response handling, for pending requests
Summary Statistics of total submissions, approvals & pending counts.
Displays requisition details in a structured format.



Code & Learning Summary
My Programs > requisitonsystem.py
My Programs contains all of my own assignment submitted work, this was easiest to reference for my git repo.	
assessment_2_software_proj_part_A.py – Functional version of the requisition system using standalone methods for staff info, requisition item entry, and approval logic.
flowchart2pseudocode.py – Simple script that transforms a logic flowchart into Python using if/else statements, testing grade classification.

Requisitionsystem.py, A complete class based system.
It includes all the methods to capture input/information from the user, calculate totals, decide approval & output summary of data. Within this script I have demonstrated my knowledge of encapsulation, class-level state tracking, clean method reuse and even conditional decision making.
Breakdown of methods in RequistionSystem()
__init__: Initializes each requisition with default values.
 generate_requisition_id: Class method to create unique identifiers.
 staff_info: Captures staff name, ID, and date using user input.
 requisitions_details: Accepts item names and costs from the user.
 requisitions_approval: Applies logic to auto-approve or mark as pending based on total cost.
 requisitions_response: Allows a manager to mark pending requests as approved or not approved.
display_requisition: Shows all requisition details formatted for clarity.
 requisition_statistics: Prints a summary of all requests and their statuses.

Supporting work – Labs Folder
In addition to my main project, I developed and commented on several smaller exercises during the term to build up my overall understanding of classes, loops and conditionals, most of which are included in my labs folder in my repo.
ClubMembership.py – Class-based member tracking system with add-on pricing and approval conditions. Helped practice dictionary input, class counters, and summary output.
helpdesk.py – IT support ticket system created by a classmate. As I missed this class, I studied his structure thoroughly and took inspiration to implement similar logic and class design in my own work. This includes ticket priority handling, auto-resolution, status tracking, and output formatting.
Im running out of time, sorry if I missed marks, here are the design principles I believe I have demonstrated and learnt throughout this course.
Encapsulation – Grouped all logic within well-defined class methods.
Reusability – Used class methods and class variables to track totals and apply logic consistently.
Object-Oriented Structure – Used class structure to simulate real-world workflows and track state.
Modularity – Broke up program logic into separate methods with one clear purpose each.
Conclusion
Through this project and supporting exercises, I demonstrated the ability to build structured, maintainable software in Python. The final requisition system integrates user input, decision-making, conditionals, and output display, all while tracking and managing multiple object instances using a class.
Each of the scripts provided have been commented, tested, and structured to reflect my learning and research into core programming principles during the term.





