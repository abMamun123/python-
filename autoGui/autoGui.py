import pyautogui
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Print the symbols
    pyautogui.typewrite('#' * i, interval=0.05)

    # Move to the next row
    pyautogui.typewrite('\n')