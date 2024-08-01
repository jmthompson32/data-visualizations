import plotly.express as px
from die import Die

# Create a D6 and a D10.
die1 = Die()
die2 = Die(10)
# Make some rolls, and store the results in a list.
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die1.num_sides + die2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    freqency = results.count(value)
    frequencies.append(freqency)

# Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Combined Dice Roll', 'y': 'Frequency of Roll'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual_d6d10.html')