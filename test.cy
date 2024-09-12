FN add(x, y)
    RETURN x + y
END
FN subtract(x, y)
    RETURN x - y
END
FN multiply(x, y)
    RETURN x * y
END
FN divide(x, y)
    IF y == 0 THEN
        RETURN "Error! Division by zero."
    ELSE
        RETURN x / y
    END
END

PRINT("SeLect operation:")
PRINT("1. Add")
PRINT("2. Subtract")
PRINT("3. Multiply")
PRINT("4. Divide")

WHILE TRUE THEN
    PRINT("Enter choice (1/2/3/4): ")
    LET choice = INPUT_INT()
       PRINT("Enter the numbers:")
        LET num1 = INPUT_INT()
        LET num2 = INPUT_INT()

        IF choice == 1 THEN
            PRINT(add(num1, num2))
        ELIF choice == 2 THEN
            PRINT(subtract(num1, num2))
        ELIF choice == 3 THEN
            PRINT(multiply(num1, num2))
        ELIF choice == 4 THEN
            PRINT(divide(num1, num2))
        BREAK
    ELSE
        PRINT("Invalid INPUT")
    END

END