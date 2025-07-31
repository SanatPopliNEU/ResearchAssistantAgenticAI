import unittest
from src.controller_agent import ControllerAgent

class TestControllerAgent(unittest.TestCase):

    def setUp(self):
        self.controller_agent = ControllerAgent()

    def test_task_delegation(self):
        # Test if the controller agent correctly delegates tasks to specialized agents
        task = "Gather information"
        assigned_agent = self.controller_agent.delegate_task(task)
        self.assertIn(assigned_agent, ["ResearchAgent", "SummarizationAgent"])

    def test_error_handling(self):
        # Test the error handling mechanism of the controller agent
        with self.assertRaises(ValueError):
            self.controller_agent.delegate_task("Invalid task")

    def test_communication_protocol(self):
        # Test the communication protocol between the controller and specialized agents
        response = self.controller_agent.communicate("Requesting data")
        self.assertEqual(response, "Data received")

    def test_fallback_mechanism(self):
        # Test the fallback mechanism when an agent fails
        self.controller_agent.specialized_agents["ResearchAgent"].fail()
        response = self.controller_agent.delegate_task("Gather information")
        self.assertEqual(response, "Fallback to SummarizationAgent")

if __name__ == '__main__':
    unittest.main()