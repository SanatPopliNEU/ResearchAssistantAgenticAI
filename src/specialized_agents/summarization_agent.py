class SummarizationAgent:
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
        return task.get("type") == "summarization"

    def handle_task(self, task):
        input_data = task.get("data")
        summary = self.summarize(input_data)
        self.maintain_context({"last_input": input_data, "last_summary": summary})
        return summary

    def process_input(self, input_data):
        # Optional: Add preprocessing logic here
        return input_data

    def generate_summary(self, processed_data):
        # Use a summarizer tool if available
        if "summarizer" in self.tools:
            return self.tools["summarizer"].summarize(processed_data)
        # Fallback: return the data as-is
        return processed_data

    def maintain_context(self, context):
        self.memory.update(context)

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory.clear()

    def receive_message(self, message):
        # Handle inter-agent communication
        pass

    def summarize(self, input_data):
        processed_data = self.process_input(input_data)
        summary = self.generate_summary(processed_data)
        return summary