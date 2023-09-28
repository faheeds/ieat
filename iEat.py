# app.py
import streamlit as st
import requests

def get_recipe_from_openai(dish_name):
    # This is a pseudo-implementation
    # For demonstration purposes, we return a mock recipe
    # In a real-world scenario, you'd call the OpenAI API or another recipe API
    mock_recipes = {
        "pasta": [
            "Pasta Recipe 1: Boil pasta. Add sauce. Serve hot.",
            "Pasta Recipe 2: Cook pasta al dente. Add olive oil and garlic. Serve."
        ],
        "pizza": [
            "Pizza Recipe 1: Spread dough. Add toppings. Bake at 425°F for 15 mins.",
            "Pizza Recipe 2: Use thin crust. Add cheese and pepperoni. Bake until crispy."
        ]
    }
    return mock_recipes.get(dish_name, [])

def main():
    st.title("Recipe Finder")
    
    dish_name = st.text_input("Enter the name of the dish:")

    if st.button("Get Recipe"):
        recipes = get_recipe_from_openai(dish_name)
        
        if recipes:
            for idx, recipe in enumerate(recipes, 1):
                st.write(f"Recipe {idx}:\n{recipe}\n")
        else:
            st.write("No recipe found!")

if __name__ == "__main__":
    main()
