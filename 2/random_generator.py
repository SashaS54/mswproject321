import mouse
#

def main():
    print("Move your mouse to generate random number.")
    mouse_coordinates = (0, 0)
    result = 1
    digits = 1
    while digits < 30:
        temp_coordinates = mouse.get_position()
        if mouse_coordinates == temp_coordinates:
            continue
        mouse_coordinates = temp_coordinates
        result *= mouse_coordinates[0] + mouse_coordinates[1]
        digits = len(str(result))
        print(f"{round(digits * 100 / 30, 2)}%")

    print(f"Your random number is: {result}")


if __name__ == "__main__":
    main()
