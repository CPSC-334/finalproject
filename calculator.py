class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero, answer is undefined.")
        return a / b
    
    def square(self, a):
        return a ** 2

    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return a ** 0.5
    
    def root(self, a, b):
        if a < 0 and b % 2 == 0:
            raise ValueError("Cannot take an even root of a negative number.")
        if a < 0 and b % 2 != 0:
            return -((-a) ** (1 / b))
        return a ** (1 / b)
    
    def logarithm(self, a, base):
        if a <= 0:
            raise ValueError("Logarithm is undefined for non-positive numbers.")
        if base <= 1:
            raise ValueError("Logarithm base must be greater than 1.")
        import math
        return math.log(a, base)

    def evaluate(self, expression):
        tokens = self._tokenize(expression.replace(' ', ''))
        result, pos = self._parse_expr(tokens, 0)
        if pos != len(tokens):
            raise ValueError("Invalid expression")
        return result

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(('NUM', float(expression[i:j])))
                i = j
            elif expression[i] in '+-*/^()':
                tokens.append(('OP', expression[i]))
                i += 1
            else:
                raise ValueError(f"Unknown character: {expression[i]}")
        return tokens

    def _parse_expr(self, tokens, pos):
        left, pos = self._parse_term(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] in ('+', '-'):
            op = tokens[pos][1]
            pos += 1
            right, pos = self._parse_term(tokens, pos)
            left = self.add(left, right) if op == '+' else self.subtract(left, right)
        return left, pos

    def _parse_term(self, tokens, pos):
        left, pos = self._parse_power(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] in ('*', '/'):
            op = tokens[pos][1]
            pos += 1
            right, pos = self._parse_power(tokens, pos)
            left = self.multiply(left, right) if op == '*' else self.divide(left, right)
        return left, pos

    def _parse_power(self, tokens, pos):
        base, pos = self._parse_unary(tokens, pos)
        if pos < len(tokens) and tokens[pos] == ('OP', '^'):
            pos += 1
            exp, pos = self._parse_power(tokens, pos)  # right-associative
            return self.power(base, exp), pos
        return base, pos

    def _parse_unary(self, tokens, pos):
        if pos < len(tokens) and tokens[pos] == ('OP', '-'):
            pos += 1
            val, pos = self._parse_atom(tokens, pos)
            return -val, pos
        return self._parse_atom(tokens, pos)

    def _parse_atom(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        tok_type, tok_val = tokens[pos]
        if tok_type == 'NUM':
            return tok_val, pos + 1
        if tok_val == '(':
            pos += 1
            val, pos = self._parse_expr(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ('OP', ')'):
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        raise ValueError(f"Unexpected token: {tok_val}")

def main():
    calculator = Calculator()
    print("Welcome to the Calculator!")
    print("Supported operations: +, -, *, /, ^ (power), sqrt (square root), log (logarithm)")
    print()
    
    while True:
        equation = input("Enter a math equation to solve (or 'quit' to exit): ").strip()
        
        if equation.lower() == 'quit':
            print("Thank you for using the Calculator!")
            break
        
        try:
            # parentheses / full expression evaluation
            if '(' in equation:
                result = calculator.evaluate(equation)
                print(f"Result: {result}\n")
                continue

            # addition
            if '+' in equation:
                parts = equation.split('+')
                result = float(parts[0])
                for part in parts[1:]:
                    result = calculator.add(result, float(part))
                print(f"Result: {result}\n")
            
            # subtraction, and handles negatives
            elif '-' in equation and not equation.startswith('-'):
                parts = equation.split('-')
                result = float(parts[0])
                for part in parts[1:]:
                    result = calculator.subtract(result, float(part))
                print(f"Result: {result}\n")
            
            # multiplication
            elif '*' in equation:
                parts = equation.split('*')
                result = float(parts[0])
                for part in parts[1:]:
                    result = calculator.multiply(result, float(part))
                print(f"Result: {result}\n")
            
            # division
            elif '/' in equation:
                parts = equation.split('/')
                result = float(parts[0])
                for part in parts[1:]:
                    result = calculator.divide(result, float(part))
                print(f"Result: {result}\n")
            
            # power
            elif '^' in equation:
                parts = equation.split('^')
                result = calculator.power(float(parts[0]), float(parts[1]))
                print(f"Result: {result}\n")
            
            # to take square root (like "sqrt64")
            elif 'sqrt' in equation:
                num = float(equation.replace('sqrt', '').strip())
                result = calculator.square_root(num)
                print(f"Result: {result}\n")

            elif 'root' in equation:
                parts = equation.split('root')
                num = float(parts[0].strip())
                degree = float(parts[1].strip())
                result = calculator.root(num, degree)
                print(f"Result: {result}\n")

            elif 'log' in equation:
                parts = equation.split('log')
                num = float(parts[0].strip())
                base = float(parts[1].strip())
                result = calculator.logarithm(num, base)
                print(f"Calculating logarithm as log base {base} of {num}...")
                print(f"Result: {result}\n")
            
            else:
                print("Invalid equation format. Please use basic operations: +, -, *, /, ^, sqrt, log\n")
        
        except ValueError as error:
            print(f"Error: {error}\n")
        except Exception as error:
            print(f"Invalid input: {error}\n")


if __name__ == "__main__":
    main()