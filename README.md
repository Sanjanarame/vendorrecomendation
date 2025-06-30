# vendorrecomendation

# UtsavAI – Smart Vendor Recommendation System

This is a smart event planning assistant that recommends the **best vendor combinations** for services like **Catering**, **Decor**, and **Photography** based on a user's **fixed budget** and **location**.

##  Project Overview

This Python-based CLI project helps users plan events by:
- Choosing their **event type** (e.g., Wedding, Birthday)
- Selecting the **location** (Bangalore, Chennai, Hyderabad, or Mumbai)
- Setting their **total budget**
- Selecting how many services they want: **1, 2, or 3**

Based on this input, the tool finds the **best vendor combinations** that fit within the budget using real-time logic and filtering.

---

##  Features

- Multiple Event Types: Wedding, Birthday, Corporate, Housewarming, Engagement
- Budget guidance per event type
- Dynamic service selection: 1, 2, or all 3 services
- Smart combination logic using `itertools.product` and `combinations`
- Filters best combos based on total cost under budget
- Works across 4 major cities
- Graceful handling when no combo fits (suggests alternatives)

---

##  Technologies Used

- Python 3
- Standard library (`itertools`)

No external libraries required. Fully terminal-based and lightweight.

---

## How to Run

1. Open vendor_recommendation.py in VS Code or any terminal-supported IDE.
2. Run the script:
```bash
python vendor_recommendation.py
