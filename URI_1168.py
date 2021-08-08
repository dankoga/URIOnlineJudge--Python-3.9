led_per_number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

tests_qty = int(input())
for t in range(tests_qty):
    leds = [led_per_number[int(digit)] for digit in input()]
    print('{} leds'.format(sum(leds)))
