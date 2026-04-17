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

def main():
    calculator = Calculator()
    print("Welcome to the Calculator!")
    print("Supported operations: +, -, *, /, ^ (power), sqrt (square root)")
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
            
            else:
                print("Invalid equation format. Please use basic operations: +, -, *, /, ^, sqrt\n")
        
        except ValueError as error:
            print(f"Error: {error}\n")
        except Exception as error:
            print(f"Invalid input: {error}\n")


if __name__ == "__main__":
    main()