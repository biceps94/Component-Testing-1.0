


def componenttesting(motorinput=0, tempinput=0):
    if motorinput < 150 and tempinput < 120:
        print("Try Again")
        return True
    elif motorinput > 150 and tempinput > 120:
        print("Game over")
        return False


def motor_and_temperature():
    try:
        motorinput = int(input("Enter the speed value of a motor:  "))
        tempinput = int(input("Enter the value of temperature: "))
        return motorinput, tempinput
    except ValueError as e:
        print("Speed and temperature must be integers")
        print(e)
        return motor_and_temperature()


def main():
    play = True
    while play:
        motorinput, tempinput = motor_and_temperature()
        play = componenttesting(motorinput, tempinput)


main()

