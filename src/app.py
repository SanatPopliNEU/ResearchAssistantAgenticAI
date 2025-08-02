import streamlit as st
from controller_agent import ControllerAgent
from specialized_agents.research_agent import ResearchAgent
from specialized_agents.summarization_agent import SummarizationAgent
from tools.web_search_tool import WebSearchTool
from tools.Summarizer_tool import SummarizerTool
from tools.output_formatting_tool import format_output
from tools.custom_domain_extractor import CustomDomainExtractor

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

# Instantiate tools and agents once
web_search = WebSearchTool(api_key=serpapi_api_key)
summarizer = SummarizerTool(api_key=openai_api_key)
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

st.title("AgenticAI System")

task = st.radio("What would you like to do?", ("Research (web search)", "Summarize text"))

if task == "Research (web search)":
    query = st.text_input("Enter your research query:")
    if st.button("Submit Research Query") and query:
        tasks = [{"type": "research", "query": query}]
        results = controller.orchestrate(tasks)
        st.subheader("Results")
        for result in results:
            if isinstance(result, list):
                for item in result:
                    st.markdown(f"**Title:** {item.get('title')}")
                    st.markdown(f"[Link]({item.get('link')})")
                    st.markdown(f"Snippet: {item.get('snippet')}")
                    st.markdown("---")
            else:
                st.write(result)
elif task == "Summarize text":
    data = st.text_area("Enter the text you want to summarize:")
    if st.button("Summarize") and data:
        tasks = [{"type": "summarization", "data": data}]
        results = controller.orchestrate(tasks)
        st.subheader("Summary")
        for result in results:
            st.write(result)