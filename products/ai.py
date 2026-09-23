from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def get_user_interest(activities):
    products = []

    for acitivity in activities:
        products.append(acitivity)

    prompt = f"""
    You are a product recommendation system.

    Available categories:
    Laptops
    Mobiles
    Fashion
    Books
    Accessories

    User acitivity:
    {products}

    Identify which one category the user is most intrested in.
    Return only one category name from the available categories.
"""

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents=prompt
    )

    category = response.text.strip()
    return category