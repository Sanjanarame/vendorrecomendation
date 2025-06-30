from itertools import product, combinations

# Vendors across 4 cities
vendors = [
    # Bangalore
    {"name": "SriLakshmiCaterers", "type": "Catering", "location": "Bangalore", "min_price": 30000},
    {"name": "SagarCater", "type": "Catering", "location": "Bangalore", "min_price": 50000},
    {"name": "BrahmiCater", "type": "Catering", "location": "Bangalore", "min_price": 70000},
    {"name": "AnilDecorz", "type": "Decor", "location": "Bangalore", "min_price": 20000},
    {"name": "RoyalDecor", "type": "Decor", "location": "Bangalore", "min_price": 40000},
    {"name": "Glittering Arc", "type": "Decor", "location": "Bangalore", "min_price": 60000},
    {"name": "SnapShotz", "type": "Photography", "location": "Bangalore", "min_price": 25000},
    {"name": "StudioH", "type": "Photography", "location": "Bangalore", "min_price": 45000},
    {"name": "Photosutra", "type": "Photography", "location": "Bangalore", "min_price": 70000},
    # Chennai
    {"name": "MadrasMeals", "type": "Catering", "location": "Chennai", "min_price": 25000},
    {"name": "VegTreats", "type": "Catering", "location": "Chennai", "min_price": 45000},
    {"name": "GrandFeast", "type": "Catering", "location": "Chennai", "min_price": 65000},
    {"name": "FloralDesigns", "type": "Decor", "location": "Chennai", "min_price": 25000},
    {"name": "SouthDecor", "type": "Decor", "location": "Chennai", "min_price": 45000},
    {"name": "ThemeWorks", "type": "Decor", "location": "Chennai", "min_price": 60000},
    {"name": "ChennaiClicks", "type": "Photography", "location": "Chennai", "min_price": 27000},
    {"name": "FrameStory", "type": "Photography", "location": "Chennai", "min_price": 50000},
    {"name": "WedCapture", "type": "Photography", "location": "Chennai", "min_price": 68000},
    # Hyderabad
    {"name": "BiryaniBites", "type": "Catering", "location": "Hyderabad", "min_price": 28000},
    {"name": "NawabiFoods", "type": "Catering", "location": "Hyderabad", "min_price": 50000},
    {"name": "RoyalKitchens", "type": "Catering", "location": "Hyderabad", "min_price": 72000},
    {"name": "DecorMania", "type": "Decor", "location": "Hyderabad", "min_price": 22000},
    {"name": "PalaceThemes", "type": "Decor", "location": "Hyderabad", "min_price": 42000},
    {"name": "GlowEvents", "type": "Decor", "location": "Hyderabad", "min_price": 62000},
    {"name": "PixelShot", "type": "Photography", "location": "Hyderabad", "min_price": 26000},
    {"name": "ZoomCraft", "type": "Photography", "location": "Hyderabad", "min_price": 47000},
    {"name": "LensKing", "type": "Photography", "location": "Hyderabad", "min_price": 69000},
    # Mumbai
    {"name": "SpicyTadka", "type": "Catering", "location": "Mumbai", "min_price": 32000},
    {"name": "BombayFeast", "type": "Catering", "location": "Mumbai", "min_price": 52000},
    {"name": "CityDelights", "type": "Catering", "location": "Mumbai", "min_price": 75000},
    {"name": "UrbanDecor", "type": "Decor", "location": "Mumbai", "min_price": 24000},
    {"name": "ClassyThemes", "type": "Decor", "location": "Mumbai", "min_price": 46000},
    {"name": "GrandEvents", "type": "Decor", "location": "Mumbai", "min_price": 63000},
    {"name": "FlashLens", "type": "Photography", "location": "Mumbai", "min_price": 27000},
    {"name": "PixelPop", "type": "Photography", "location": "Mumbai", "min_price": 48000},
    {"name": "ShutterEye", "type": "Photography", "location": "Mumbai", "min_price": 70000},
]

event_budgets = {
    "wedding": "₹3,00,000 and above",
    "engagement": "₹2,00,000 and above",
    "housewarming": "₹1,00,000 – ₹1,50,000",
    "birthday": "₹50,000 – ₹1,00,000",
    "corporate": "₹1,50,000 and above"
}

def group_vendors(location):
    grouped = {"Catering": [], "Decor": [], "Photography": []}
    for v in vendors:
        if v["location"].lower() == location.lower():
            grouped[v["type"]].append(v)
    return grouped

def flexible_combos(grouped, budget, service_count):
    categories = list(grouped.keys())
    all_service_sets = list(combinations(categories, service_count))
    results = []

    for service_set in all_service_sets:
        vendor_lists = [grouped[cat] for cat in service_set]
        for combo in product(*vendor_lists):
            total = sum(v["min_price"] for v in combo)
            if total <= budget:
                results.append((total, combo))

    results.sort(reverse=True, key=lambda x: x[0])
    return results[:3]

def print_combos(combos):
    if not combos:
        print("\nNo vendor combination fits within your budget.")
        print("Try increasing your budget or selecting fewer services.")
        return
    for idx, (total, combo) in enumerate(combos, start=1):
        print(f"\nCombo {idx} (Total: ₹{total})")
        for v in combo:
            print(f"{v['type']:<12}: {v['name']:<15} ₹{v['min_price']}")

# ==== User Input ====
print("Event Types: Wedding, Birthday, Corporate, Housewarming, Engagement")
event_type = input("Enter event type: ").strip().lower()

if event_type in event_budgets:
    print(f"Suggested budget for {event_type.capitalize()}: {event_budgets[event_type]}")
else:
    print("No suggested budget available for this event type.")

budget = int(input("Enter your total budget (₹): "))

print("Available Locations: Bangalore, Chennai, Hyderabad, Mumbai")
location = input("Enter event location: ").strip()

print("Select number of services (1 = Catering or Decor or Photography, 2 = any two, 3 = all three)")
services = int(input("Enter number of services to include (1, 2, or 3): "))
if services < 1 or services > 3:
    print("Invalid service count. Defaulting to 3.")
    services = 3

# ==== Process ====
grouped = group_vendors(location)
combos = flexible_combos(grouped, budget, services)

print("\nBest Vendor Combinations Based on Your Input:")
print_combos(combos)
