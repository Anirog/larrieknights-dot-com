import json
import os
from jinja2 import Environment, FileSystemLoader

def get_span(card):
    try:
        return int(card['widthClass'].split('-')[1])
    except (KeyError, IndexError, ValueError):
        return 4  # fallback span

def group_cards(cards):
    rows = []
    current_row = []
    current_sum = 0

    for card in cards:
        span = get_span(card)

        if span > 12:
            if current_row:
                # Fill incomplete row before large card
                if current_sum < 12:
                    filler = {"widthClass": f"span-{12 - current_sum}", "is_filler": True}
                    current_row.append(filler)
                rows.append(current_row)
            rows.append([card])
            current_row = []
            current_sum = 0
            continue

        if current_sum + span > 12:
            if current_sum < 12:
                filler = {"widthClass": f"span-{12 - current_sum}", "is_filler": True}
                current_row.append(filler)
            rows.append(current_row)
            current_row = [card]
            current_sum = span
        else:
            current_row.append(card)
            current_sum += span

    if current_row:
        if current_sum < 12:
            filler = {"widthClass": f"span-{12 - current_sum}", "is_filler": True}
            current_row.append(filler)
        rows.append(current_row)

    return rows

# Set paths
base_dir = os.path.dirname(__file__)
cards_dir = os.path.join(base_dir, 'cards')
json_path = os.path.join(cards_dir, 'cards.json')
template_path = os.path.join(cards_dir, 'card-template.html')
output_path = os.path.join(cards_dir, 'index.html')

# Load data
with open(json_path, 'r') as f:
    all_cards = json.load(f)
    cards = [card for card in all_cards if card.get('featured') is True]
    rows = group_cards(cards)

# Set up Jinja
env = Environment(loader=FileSystemLoader(cards_dir))
template = env.get_template('card-template.html')

import pprint
pprint.pprint([[get_span(c) for c in row] for row in rows])

# Render HTML
output = template.render(rows=rows)

# Write output
with open(output_path, 'w') as f:
    f.write(output)

print("✅ cards/index.html generated.")