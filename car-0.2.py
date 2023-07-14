import motor_pair
import runloop
from hub import port


async def main():
    # Setup the movement motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motor_pair.pair(motor_pair.PAIR_2, port.C, port.D)

while True:
    # Move straight at default velocity
    motor_pair.move_tank(motor_pair.PAIR_1, 500, 500)
    motor_pair.move_tank(motor_pair.PAIR_1, 500, 500)

    # Perform tank turn for 5 seconds
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 5000)

runloop.run(main())
