import openai

class SummarizerTool:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def summarize(self, data):
        if not isinstance(data, str):
            data = str(data)
        prompt = f"Summarize the following text in a concise and clear way:\n\n{data}"
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=256,
                temperature=0.5,
            )
            summary = response.choices[0].message.content.strip()
            return summary
        except Exception as e:
            return f"Error during summarization: {e}"