from controller_agent import ControllerAgent
from specialized_agents.research_agent import ResearchAgent
from specialized_agents.summarization_agent import SummarizationAgent
from tools.web_search_tool import WebSearchTool
from tools.Summarizer_tool import SummarizerTool
from tools.output_formatting_tool import format_output
from tools.custom_domain_extractor import CustomDomainExtractor

def main():
    # Instantiate tools and agents once
    web_search = WebSearchTool(api_key="9b87a30ced28672585d1d6c894421ccda9778ee0bd84fbf61ce9f46738a83487")
    summarizer = SummarizerTool()
    custom_extractor = CustomDomainExtractor()

    research_agent = ResearchAgent(tools={
        "web_search": web_search,
        "summarizer": summarizer,
        "extractor": custom_extractor
    })
    summarization_agent = SummarizationAgent(tools={
        "summarizer": summarizer
    })

    controller = ControllerAgent()
    controller.register_agent("research", research_agent)
    controller.register_agent("summarization", summarization_agent)

    print("Welcome to AgenticAI System!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Research (web search)")
        print("2. Summarize text")
        print("Q. Quit")
        choice = input("Enter 1, 2, or Q: ").strip().lower()

        if choice == "1":
            query = input("Enter your research query: ").strip()
            tasks = [{"type": "research", "query": query}]
        elif choice == "2":
            data = input("Enter the text you want to summarize: ").strip()
            tasks = [{"type": "summarization", "data": data}]
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        results = controller.orchestrate(tasks)
        print("\n--- Result ---")
        for result in results:
            if isinstance(result, list):
                for item in result:
                    print(f"\nTitle: {item.get('title')}")
                    print(f"Link: {item.get('link')}")
                    print(f"Snippet: {item.get('snippet')}")
                    print("-" * 40)
            else:
                print(result)

if __name__ == "__main__":
    main()