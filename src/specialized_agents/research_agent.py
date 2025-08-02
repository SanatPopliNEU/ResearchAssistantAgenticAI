class ResearchAgent:
    def __init__(self, tools=None):
        self.objectives = []
        self.success_criteria = []
        self.memory = {}
        self.tools = tools or {}

    def set_objectives(self, objectives):
        self.objectives = objectives

    def set_success_criteria(self, criteria):
        self.success_criteria = criteria

    def can_handle(self, task):
        return task.get("type") == "research"

    def handle_task(self, task):
      query = task.get("query")
      info = self.gather_information(query)
      print("DEBUG: info from web search:", info)
      self.maintain_contextual_awareness({"last_query": query, "last_result": info})
      return info  # Return the raw search results

    def gather_information(self, query):
        # Use web search tool if available
        if "web_search" in self.tools:
            return self.tools["web_search"].search(query)
        return f"No web_search tool available for query: {query}"

    def analyze_information(self, data):
        # Use summarizer tool if available
        if "summarizer" in self.tools:
            return self.tools["summarizer"].summarize(data)
        return data

    def maintain_contextual_awareness(self, context):
        self.memory.update(context)

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory.clear()

    def receive_message(self, message):
        # Handle inter-agent communication
        pass