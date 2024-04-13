def evaluate_homework():
    import re

    print("Enter arithmetic problems and their answers line by line (e.g., '40*30=1200').")
    print("Type 'done' when you have finished entering problems.")

    # Collect all problems
    problems = []
    while True:
        problem = input()
        if problem.lower() == 'done':
            break
        problems.append(problem)

    # Process each problem
    for problem in problems:

        # Print the input.
        #print(problem)

        # Regular expression to match the problem format (operand-operator-operand=answer)
        match = re.match(r'(\ *\d+)\s*([+*/-])\s*(\d+)\s*=\s*(\d+)', problem)

        if not match:
            #print("Invalid format or input. Please ensure the format is: a * b = c")
            continue

        # Extract operands, operator, and the student's answer
        operand1, operator, operand2, student_answer = match.groups()
        operand1 = int(operand1)
        operand2 = int(operand2)
        student_answer = int(student_answer)
        #print("Operand 1 = ", operand1, "  Operand 2 = ", operand2, "  Student answer = ", student_answer)
        # Calculate the correct answer based on the operator
        if operator == '+':
            correct_answer = operand1 + operand2
        elif operator == '-':
            correct_answer = operand1 - operand2
        elif operator == '*':
            correct_answer = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                print("Division by zero is not allowed.")
                continue
            correct_answer = operand1 // operand2  # Using integer division

        # Compare the student's answer with the correct answer
        if student_answer == correct_answer:
             print(problem, "ok")
        else:
            print(problem, f"    X The answer is {correct_answer} (difference is {student_answer-correct_answer})")

# Run the function
evaluate_homework()


# def evaluate_homework():
#     import re
#
#     while True:
#         # Input the arithmetic problem and the student's answer
#         problem = input("Enter an arithmetic problem and answer (e.g., '40*30=1200'), or type 'exit' to quit: ")
#
#         if problem.lower() == 'exit':
#             break

#         # Regular expression to match the problem format (operand-operator-operand=answer)
#         match = re.match(r'(\ *\d+)\s*([+*/-])\s*(\d+)\s*=\s*(\d+)', problem)
#
#         if not match:
#             print("Invalid format. Please use the format: a * b = c")
#             continue
#
#         # Extract operands, operator, and the student's answer
#         operand1, operator, operand2, student_answer = match.groups()
#         operand1 = int(operand1)
#         operand2 = int(operand2)
#         student_answer = int(student_answer)
#         print("Operand 1 = ", operand1, "  Operand 2 = ", operand2, "  Student answer = ", student_answer)
#
#         # Calculate the correct answer based on the operator
#         if operator == '+':
#             correct_answer = operand1 + operand2
#         elif operator == '-':
#             correct_answer = operand1 - operand2
#         elif operator == '*':
#             correct_answer = operand1 * operand2
#         elif operator == '/':
#             # Handle division by zero
#             if operand2 == 0:
#                 print("Division by zero is not allowed.")
#                 continue
#             correct_answer = operand1 // operand2  # Using integer division
#
#         # Compare the student's answer with the correct answer
#         if student_answer == correct_answer:
#             print("Correct!")
#         else:
#             print(f"Incorrect. The correct answer is {correct_answer}.")
#
# # Run the function
# evaluate_homework()
