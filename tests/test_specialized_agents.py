import unittest
from src.specialized_agents.research_agent import ResearchAgent
from src.specialized_agents.summarization_agent import SummarizationAgent

class TestSpecializedAgents(unittest.TestCase):

    def setUp(self):
        self.research_agent = ResearchAgent()
        self.summarization_agent = SummarizationAgent()

    def test_research_agent_objectives(self):
        self.research_agent.set_objectives("Gather information on AI systems.")
        self.assertEqual(self.research_agent.objectives, "Gather information on AI systems.")

    def test_research_agent_success_criteria(self):
        self.research_agent.set_success_criteria("Collect at least 5 credible sources.")
        self.assertEqual(self.research_agent.success_criteria, "Collect at least 5 credible sources.")

    def test_summarization_agent_summary_generation(self):
        input_data = "Artificial Intelligence (AI) is intelligence demonstrated by machines."
        expected_summary = "AI is intelligence shown by machines."
        self.summarization_agent.process_input(input_data)
        self.assertEqual(self.summarization_agent.generate_summary(), expected_summary)

    def test_summarization_agent_contextual_awareness(self):
        self.summarization_agent.set_context("AI technologies are evolving rapidly.")
        self.assertEqual(self.summarization_agent.context, "AI technologies are evolving rapidly.")

if __name__ == '__main__':
    unittest.main()