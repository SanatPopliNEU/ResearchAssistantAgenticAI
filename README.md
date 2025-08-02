# AgenticAI System

## Overview

AgenticAI System is a modular, multi-agent research assistant built in Python.  
It demonstrates agentic AI design principles, including multi-agent orchestration, tool integration, and domain-specific information extraction.  
The system features a user-friendly Streamlit web interface and can also be run as a CLI.

---

## Features

- **Multi-agent orchestration** with a central ControllerAgent
- **ResearchAgent** for web search and information extraction
- **SummarizationAgent** for text summarization
- **Integration of three built-in tools:**  
  - WebSearchTool (SerpAPI)
  - SummarizerTool (OpenAI API)
  - OutputFormattingTool
- **CustomDomainExtractor** for domain-specific information extraction
- **Extensible architecture** for adding new agents or tools

---

## Architecture

<img width="1116" height="611" alt="Agentic AI Diagram" src="https://github.com/user-attachments/assets/f927065f-a8c5-4e0a-bb4d-f9f473caf1e0" />


## File Structure

```
agentic-system/
│
├── src/
│   ├── app.py
│   ├── controller_agent.py
│   ├── specialized_agents/
│   │   ├── research_agent.py
│   │   └── summarization_agent.py
│   └── tools/
│       ├── web_search_tool.py
│       ├── summarizer_tool.py
│       ├── output_formatting_tool.py
│       └── custom_domain_extractor.py
├── .env
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone <your-repo-url>
    cd agentic-system
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your `.env` file** in the project root:
    ```
    OPENAI_API_KEY=your-openai-api-key
    SERPAPI_API_KEY=your-serpapi-api-key
    ```

4. **Run the Streamlit app**
    ```sh
    streamlit run src/app.py
    ```

---

## Usage

### Web Interface

- **Research (web search):**  
  Enter a query to get a list of relevant articles (title, link, snippet).
- **Summarize text:**  
  Paste any text to get a concise summary.

### CLI (if implemented)

- Follow the prompts to choose between research and summarization.

---

## Agent & Tool Descriptions

### ControllerAgent
- Orchestrates tasks and delegates to the appropriate agent.

### ResearchAgent
- Handles research queries.
- Uses:
  - **WebSearchTool:** Fetches search results from SerpAPI.
  - **SummarizerTool:** (Optional) Summarizes results if needed.
  - **CustomDomainExtractor:** Extracts domain-specific information.

### SummarizationAgent
- Handles text summarization using SummarizerTool.

### Tools
- **WebSearchTool:** Integrates with SerpAPI to fetch web results.
- **SummarizerTool:** Uses OpenAI API to generate summaries.
- **CustomDomainExtractor:** Custom tool for extracting domain-specific info.
- **OutputFormattingTool:** Formats output for display.

---

## Custom Tool: CustomDomainExtractor

- **Purpose:** Extracts domain-specific information from research results.
- **Inputs:** Raw search results (list of dicts).
- **Outputs:** Filtered or highlighted information relevant to the chosen domain.
- **Limitations:** Extraction logic may need tuning for different domains.

---

## Evaluation

- **Tested with various queries and texts.**
- **Metrics considered:** Accuracy, relevance, and response time.
- **Error handling:** Robust to API failures and missing data.
- **Extensible:** Easily add new agents or tools.

---

## Challenges & Solutions

- **API quota management:** Handled by using environment variables and error handling.
- **Result formatting:** Used a dedicated formatting tool for clean UI.
- **Extensibility:** Modular design for easy addition of new features.

---

## Limitations & Future Work

- **Web search limited by SerpAPI quota and coverage.**
- **Summarization limited by OpenAI API quota.**
- **Future:** Add more agents, support more domains, improve extraction logic, and add feedback loops for agent improvement.

---

## License

MIT License (or your chosen license)

---

## Acknowledgements

- [OpenAI](https://openai.com/)
- [SerpAPI](https://serpapi.com/)
- [Streamlit](https://streamlit.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

*For any questions, please contact [your-email@example.com].*
