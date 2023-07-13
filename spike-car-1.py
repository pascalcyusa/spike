# This program will run the motors until a certain color is detected.

from hub import port 
import color
import color_sensor
import runloop
import motor_pair

# Pair the two motors
motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():
    while True:
        # Move straight at default velocity
        motor_pair.move_tank(motor_pair.PAIR_1, 500, 500)

        # Check if a color is detected and stop the motors
        if color_sensor.color(port.B) == color.YELLOW:
            motor_pair.stop(motor_pair.PAIR_1)  
            while True: 
                motor_pair.move_tank(motor_pair.PAIR_1, -500, -500)
                if color_sensor.color(port.A) == color.YELLOW:
                    motor_pair.stop(motor_pair.PAIR_1)
                motor_pair.move_tank(motor_pair.PAIR_1, 500, 500)
runloop.run(main())

