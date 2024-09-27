import requests

def bing_image_search(query, subscription_key, count=50):
    search_url = "https://api.bing.microsoft.com/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "license": "public", "imageType": "photo", "count": count}
    
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return [(img["contentUrl"], img["name"]) for img in search_results["value"]]

# Example usage:
if __name__ == "__main__":
    subscription_key = "YOUR_BING_SEARCH_API_KEY"
    food_images = bing_image_search("pizza", subscription_key)
    for url, name in food_images:
        print(f"Image URL: {url}, Name: {name}")
