# =====================================================
# -------------- Dice Rolling Simulator ---------------
# =====================================================

import random



dice_one = """
+---------+
|         |
|    ○    |
|         |
+---------+
"""
dice_two = """
+---------+
| ○       |
|         |
|       ○ |
+---------+
"""
dice_three = """
+---------+
| ○       |
|    ○    |
|       ○ |
+---------+
"""

dice_four = """
+---------+
| ○     ○ |
|         |
| ○     ○ |
+---------+
"""

dice_five = """
+---------+
| ○     ○ |
|    ○    |
| ○     ○ |
+---------+
"""

dice_six = """
+---------+
| ○     ○ |
| ○     ○ |
| ○     ○ |
+---------+
"""


rolling_dices = int(input('How many dices would you like to roll? '))




dice_sides = [dice_one, dice_two, dice_three,
              dice_four, dice_five, dice_six]

for i in range(rolling_dices):
    rolled_number = random.randint(0, 5)
    print(dice_sides[rolled_number])
