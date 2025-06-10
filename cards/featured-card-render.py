import json
from jinja2 import Environment, FileSystemLoader

# Step 1: Load the card data from JSON
with open('featuredcards.json', 'r') as f:
    cards = json.load(f)

# Step 2: Set up Jinja2 to load from current folder
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('featured-card-template.html')

# Step 3: Pick the first card
card = cards[0]

# Step 4: Render the template using that card
output = template.render(card=card)

# Step 5: Save the result to an HTML file
with open('featured-card.html', 'w') as f:
    f.write(output)