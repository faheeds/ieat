# app.py
import streamlit as st
import requests

def get_recipe_from_openai(dish_name):
    # Access the API key from Streamlit secrets
    api_key = st.secrets["OPENAI_API_KEY"]

    # Define your OpenAI API endpoint and authentication
    endpoint = "https://api.openai.com/search"  # Replace with the actual endpoint
    headers = {
        "Authorization": api_key
    }
    # Define your search query
    query = {
        "q": f"{dish_name} recipe",
        "size": 2  # get top 2 results
    }
    # Make the API call
    response = requests.get(endpoint, headers=headers, params=query)
    st.write(f"API Response: {response.json()}")  # Add this line to print the response to the Streamlit app
    # Check for successful response
    if response.status_code == 200:
        results = response.json().get("results", [])
        if not results:
            return None
        else:
            # Extract the top 2 recipes (assuming there's a "recipe" field in the response)
            top_recipes = [result.get("recipe") for result in results[:2]]
            return top_recipes
    else:
        print("Error:", response.status_code)
        return None

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
