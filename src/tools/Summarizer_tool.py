class SummarizerTool:
    def summarize(self, data):
        # Simple summarization: return the first 2 sentences or items
        if isinstance(data, list):
            return data[:2]
        elif isinstance(data, str):
            sentences = data.split('.')
            return '.'.join(sentences[:2]) + '.' if len(sentences) > 1 else data
        else:
            return data