import requests

class WebSearchTool:
    def __init__(self, api_key, api_url="https://serpapi.com/search"):
        self.api_key = api_key
        self.api_url = api_url

    def search(self, query):
        params = {
            'q': query,
            'api_key': self.api_key,
            'engine': 'google',
        }
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            results = response.json()
            # You can adjust this depending on what data you want from the results
            return results.get('organic_results', [])
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the web search: {e}")
            return []

# Example usage
if __name__ == "__main__":
    api_key = "9b87a30ced28672585d1d6c894421ccda9778ee0bd84fbf61ce9f46738a83487"  # Replace with your real key
    tool = WebSearchTool(api_key)
    query = "agentic AI systems"
    search_results = tool.search(query)
    print(search_results)