from specialized_agents.research_agent import ResearchAgent
from specialized_agents.summarization_agent import SummarizationAgent
from tools.web_search_tool import perform_search
from tools.data_processing_tool import process_data
from tools.output_formatting_tool import format_output
from memory.memory_manager import MemoryManager

class Workflow:
    def __init__(self):
        self.memory_manager = MemoryManager()
        self.research_agent = ResearchAgent()
        self.summarization_agent = SummarizationAgent()

    def execute_workflow(self, query):
        # Step 1: Research phase
        search_results = perform_search(query)
        self.memory_manager.store_memory('search_results', search_results)

        # Step 2: Data processing
        processed_data = process_data(search_results)
        self.memory_manager.store_memory('processed_data', processed_data)

        # Step 3: Summarization
        summary = self.summarization_agent.summarize(processed_data)
        self.memory_manager.store_memory('summary', summary)

        # Step 4: Format output
        formatted_output = format_output(summary)
        return formatted_output

    def feedback_loop(self, user_feedback):
        # Implement feedback mechanism to improve agent performance
        self.research_agent.update_based_on_feedback(user_feedback)
        self.summarization_agent.update_based_on_feedback(user_feedback)

    def manage_memory(self):
        # Manage memory to ensure contextual awareness
        self.memory_manager.cleanup_memory()