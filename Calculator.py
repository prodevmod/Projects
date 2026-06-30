def calculate(expression):
    operands = []
    operators = []

    # Helper function for performing the calculation
    def perform_operation():
        operator = operators.pop()
        right = operands.pop()
        left = operands.pop()
        if operator == '+':
            result = left + right
        else:
            result = left - right
        operands.append(result)

    # Remove whitespaces from expression
    expression = expression.replace(' ', '')

    # Start parsing the expression
    num = ''
    for char in expression:
        if char.isdigit():
            num += char
        else:
            operands.append(int(num))
            num = ''
            if char in '+-':
                while operators and operators[-1] != '(':
                    perform_operation()
                operators.append(char)
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    perform_operation()
                operators.pop()
            
    operands.append(int(num))  # Add the last number to the operands list
    
    while operators:
        perform_operation()

    return operands[0]
