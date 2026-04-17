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