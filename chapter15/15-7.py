import pygal

from die import Die

# Create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1,000,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')