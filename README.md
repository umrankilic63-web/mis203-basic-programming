 # MIS203 Basic Programming

## Week 01

## Student Information

- Name: Ümran Kılıç
- Student Number: 2404109051
- Department: Management Information Systems
- Career Goal: Data Analyst

## AI Tool Used

**AI Tool Used:** ChatGPT

**Prompt Used:** Create a simple Python program that asks the user for their name, department, age, and career goal, then prints a short student profile.

**What did you change?** I changed the program according to my own information and checked how the input and print functions work.

## Week 02

**AI Tool Used:** ChatGPT

**Prompt Used:** Write a Python program named grade_calculator.py that uses while True and break. Ask for a student name and score, check if the score is between 0 and 100, calculate the letter grade, print the result, and calculate the total number of students and average score.

**What did you change?** I changed the code to keep track of the total number of students and their scores. I also tested the program with different scores.

**What does break do in your program?** The break statement stops the loop when the user enters q.

## Week 03

- **AI Tool Used:** ChatGPT

- **Prompt Used:** Create a Python cinema ticket office program that asks for customer name, age, day, and student status. Validate age, day, and student input, apply the specified ticket pricing rules in order, print each ticket result with two decimal places, and print a summary of tickets sold, total revenue, average price, and free tickets.

- **What did you change?** I changed the code step by step and tested the program with different ages, days, and student answers. I also checked boundary ages to make sure the discount rules work correctly.

- **Tests:**
  1. Input: Age 65, weekday, not a student → Result: 100.00 TRY (Senior)
  2. Input: Age 12, weekend, student → Result: 150.00 TRY (Child)
  3. Input: Age 20, weekday, student → Result: 140.00 TRY (Student)

- **Why does the order of the rules matter?** The program applies only the first matching rule. For example, a 10-year-old student must get the Child discount, so the Child rule must come before the Student rule.
