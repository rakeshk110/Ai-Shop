from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def get_user_interest(activities):

    try:
        products = []

        for activity in activities:
            products.append(activity.product.name)

        prompt = f"""
        You are a product recommendation system.

        Available categories:
        Laptop
        Mobiles
        Fashion
        Books
        Accessories

        User activity:
        {products}

        Identify which ONE category the user is most interested in.

        Return ONLY one category name from the available categories.
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print("Gemini API Error:", e)
        return None