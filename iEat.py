import streamlit as st
import openai

# Initialize the OpenAI API with your key from Streamlit secrets
openai.api_key = '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'

def get_recipe_from_openai(dish_name):
    # Construct the message to get a recipe
    message = {
        'role': 'user',
        'content': f"Please provide a detailed recipe for {dish_name}."
    }

    # Get the response from the OpenAI model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[message]
    )
    
    # Extract the recipe from the response
    recipe = response.choices[0].message['content'].strip()
    
    # Return the recipe or None if not found
    return recipe if recipe else None

def main():
    st.title("Recipe Finder")
    
    dish_name = st.text_input("Enter the name of the dish:")
    if st.button("Get Recipe"):
        recipe = get_recipe_from_openai(dish_name)
        
        if recipe:
            st.write(f"Recipe for {dish_name}:\n{recipe}\n")
        else:
            st.write("No recipe found!")

if __name__ == "__main__":
    main()
