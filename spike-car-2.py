from hub import port
import color
import color_sensor
import motor
import runloop


async def main():
    # Move forward at default velocity
    motor.run(port.A, -500)
    motor.run(port.B, 500)
    motor.run(port.C, 500)
    motor.run(port.D, -500)

    while color_sensor.color(port.E) != color.GREEN or color_sensor.color(port.E) != color.BLACK:
        # When front sensor detects a color, stop and reverse direction
        if color_sensor.color(port.E) == color.GREEN or color_sensor.color(port.E) == color.BLACK:
            motor.run(port.A, 500)
            motor.run(port.B, -500)
            motor.run(port.C, -500)
            motor.run(port.D, 500)

        # When back sensor detects a color, stop and reverse direction
        if color_sensor.color(port.F) == color.GREEN or color_sensor.color(port.F) == color.BLACK:
            motor.run(port.A, -500)
            motor.run(port.B, 500)
            motor.run(port.C, 500)
            motor.run(port.D, -500)

runloop.run(main())
