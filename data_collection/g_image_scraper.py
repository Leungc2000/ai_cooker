import requests
from bs4 import BeautifulSoup
import os

common_ingredients_global = [
    "Raw whole chicken", "Raw chicken breasts", "Raw chicken thighs", "Raw ground beef", "Raw pork chops",
    "Raw pork belly", "Raw bacon", "Raw beef steak", "Raw lamb leg", "Raw ground turkey",
    "Raw salmon fillets", "Raw tuna steaks", "Raw cod fillets", "Raw shrimp", "Raw scallops",
    "Eggs", "Butter", "Cheddar cheese", "Parmesan cheese", "Mozzarella cheese",
    "Whole milk", "Skim milk", "Heavy cream", "Plain yogurt", "Greek yogurt",
    "Olive oil", "Vegetable oil", "Canola oil", "Sesame oil", "Coconut oil",
    "White rice", "Brown rice", "Basmati rice", "Quinoa", "Couscous",
    "Spaghetti pasta", "Penne pasta", "Rice noodles", "Whole wheat bread", "White bread",
    "Raw garlic cloves", "Raw ginger root", "Raw yellow onions", "Raw red onions", "Raw green onions",
    "Raw russet potatoes", "Raw sweet potatoes", "Raw carrots", "Raw broccoli", "Raw cauliflower",
    "Raw spinach", "Raw kale", "Romaine lettuce", "Raw cucumbers", "Raw zucchini",
    "Raw tomatoes", "Raw cherry tomatoes", "Raw bell peppers", "Raw jalapeno peppers", "Raw habanero peppers",
    "Raw lemons", "Raw limes", "Raw apples", "Raw bananas", "Raw oranges",
    "Raw blueberries", "Raw strawberries", "Raw mangoes", "Raw pineapples", "Raw avocados",
    "Raw almonds", "Raw walnuts", "Raw peanuts", "Raw cashews", "Raw pistachios",
    "Raw black beans", "Raw lentils", "Raw chickpeas", "Raw kidney beans", "Raw navy beans",
    "Soy sauce", "Hot sauce", "Tomato sauce", "Barbecue sauce", "Mayonnaise",
    "Sea salt", "Black peppercorns", "Cumin seeds", "Coriander seeds", "Turmeric powder",
    "Cinnamon sticks", "Vanilla extract", "Cocoa powder", "Baking powder", "Baking soda",
    "Honey", "Maple syrup", "Granulated sugar", "Brown sugar", "Powdered sugar"
]


def fetch_images(query, num_images):
    query = query.replace(' ', '+')  # Format the query for URL
    url = f"https://www.google.com/search?tbm=isch&q={query}"
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = [img['src'] for img in soup.find_all('img') if img.get('src') and 'http' in img['src']]
        
        # Limit the number of images to num_images
        images = images[:num_images]
        return images
    else:
        print(f"Failed to retrieve HTML content for {query}")
        return []

def download_image(url, folder_path, name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(folder_path, f"{name}.jpg")
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filepath}")
    else:
        print(f"Failed to download image from {url}")

def main():
    ingredients = common_ingredients_global  # List of ingredients
    num_images = 20  # Number of images you want to download for each ingredient
    
    for ingredient in ingredients:
        folder_path = f"downloaded_images/{ingredient}"  # Folder for each ingredient
        images = fetch_images(ingredient, num_images)
        for index, img_url in enumerate(images):
            name = f"{ingredient}_{str(index + 1).zfill(3)}"  # Filename like "ingredient_name_001"
            download_image(img_url, folder_path, name)

if __name__ == "__main__":
    main()
