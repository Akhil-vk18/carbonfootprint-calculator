import streamlit as st

def print_suggestion(category):
    if category == "Transportation":
        suggestions = [
            "1. Consider using public transportation, carpooling, or biking for daily commute.",
            "2. If possible, switch to an electric or hybrid vehicle.",
            "3. Reduce air travel and opt for video conferencing instead.",
            "4. Maintain your vehicle in good condition to improve fuel efficiency.",
            "5. Explore local travel options instead of long-distance trips.",
        ]
    elif category == "Electricity":
        suggestions = [
            "1. Switch to renewable energy sources like solar or wind power.",
            "2. Reduce energy consumption by using energy-efficient appliances.",
            "3. Turn off lights, electronics, and appliances when not in use.",
            "4. Use a programmable thermostat to manage heating and cooling costs.",
            "5. Insulate your home to reduce heating and cooling needs.",
        ]
    elif category == "Diet":
        suggestions = [
            "1. Reduce meat consumption, especially red meat, and opt for plant-based meals.",
            "2. Buy locally grown and produced food to reduce transportation emissions.",
            "3. Avoid food waste by planning meals and using leftovers.",
            "4. Grow your own vegetables and herbs to reduce carbon footprint.",
            "5. Choose organic and seasonal food options.",
        ]
    elif category == "Waste":
        suggestions = [
            "1. Reduce, reuse, and recycle waste to minimize landfill contributions.",
            "2. Compost organic waste like food scraps and yard waste.",
            "3. Avoid single-use plastics and opt for reusable items.",
            "4. Buy in bulk or choose products with minimal packaging.",
            "5. Donate or sell items you no longer need instead of throwing them away.",
        ]
    else:
        suggestions=["No suggestions for this category"]

    return "\n".join(suggestions)