def safe_division():
    """
    Demonstrates robust exception handling by taking user inputs,
    performing division, and safely managing common runtime errors.
    """
    print("--- Safe Division Program Started ---")
    
    try:
        # 1. Code that might raise an exception
        numerator = int(input("Enter the numerator (number to divide): "))
        denominator = int(input("Enter the denominator (number to divide by): "))
        
        result = numerator / denominator

    except ValueError as error:
        # 2. Catches invalid input types (e.g., entering letters instead of numbers)
        print(f"Input Error: Please enter valid integers only. Details: {error}")

    except ZeroDivisionError as error:
        # 3. Catches division by zero errors
        print(f"Math Error: You cannot divide a number by zero. Details: {error}")

    except Exception as error:
        # 4. Fallback block to catch any other unexpected exceptions
        print(f"Unexpected Error occurred: {error}")

    else:
        # 5. Executes ONLY if no exceptions were raised in the try block
        print(f"Success! The result of the division is: {result}")

    finally:
        # 6. ALWAYS executes, regardless of whether an error occurred or not
        print("Cleanup: Closing program resources safely.")
        print("--- Safe Division Program Ended ---\n")

# Run the program
if __name__ == "__main__":
    safe_division()
    print("Program continues to run after handling exceptions gracefully.")



# BaseException                   ← catch ONLY at top-level or in frameworks
#   ├── SystemExit                  ← raised by sys.exit() — don't swallow!
#   ├── KeyboardInterrupt           ← Ctrl+C — don't swallow!
#   ├── GeneratorExit               ← generator .close() — don't swallow!
#   └── Exception                  ← catch THIS in normal application code
#       ├── ArithmeticError
#       │   ├── ZeroDivisionError
#       │   └── OverflowError
#       ├── LookupError
#       │   ├── IndexError          ← list[100] on a 3-element list
#       │   └── KeyError            ← dict['missing_key']
#       ├── ValueError              ← int('abc'), wrong value for the type
#       ├── TypeError               ← wrong type: '5' + 5
#       ├── AttributeError         ← None.split() — object has no attribute
#       ├── NameError              ← undefined variable
#       ├── OSError (IOError)      ← OS-level problems
#       │   ├── FileNotFoundError
#       │   ├── PermissionError
#       │   └── IsADirectoryError
#       ├── RuntimeError
#       │   └── RecursionError
#       └── StopIteration          ← end of iterator — GeneratorExit related