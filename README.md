# AgenticAI System (ResearchAI Assistant)

## Overview

AgenticAI System is a modular, multi-agent research assistant built in Python.  
It demonstrates agentic AI design principles, including multi-agent orchestration, tool integration, and domain-specific information extraction.  
The system features a user-friendly Streamlit web interface and can also be run as a CLI.

---

## Learning Objectives

- Understand the architecture of agentic AI systems
- Implement a controller agent that orchestrates task delegation
- Integrate both pre-built and custom tools into an agentic workflow
- Apply reinforcement learning concepts to improve agent performance (future work)
- Evaluate agentic system effectiveness through metrics and testing

---

## Application Domain

**Domain:** ResearchAI Assistant  
- Gathers, analyzes, and synthesizes information from the web  
- Tools for web search, content summarization, and output formatting  
- Custom tool for domain-specific information extraction

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
- **Memory management** for contextual awareness
- **Error handling** and fallback mechanisms
- **Communication protocol** between agents

---

## Architecture

<img width="1116" height="611" alt="Agentic AI Diagram" src="https://github.com/user-attachments/assets/dce5e8c9-61d9-449a-ba7b-223b19db7d12" />


---

## File Structure

```
agentic-system/
│
├── src/
│   ├── app.py
│   ├── main.py
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

## APIs, Libraries, and Technologies Used

### APIs
- **OpenAI API:**  
  Used for text summarization via GPT-3.5-turbo.  
  API key stored as `OPENAI_API_KEY` in `.env`.
- **SerpAPI:**  
  Used for web search and retrieval of article titles, links, and snippets.  
  API key stored as `SERPAPI_API_KEY` in `.env`.

### Python Libraries
- **streamlit:** For the web interface.
- **requests:** For HTTP requests to SerpAPI.
- **openai:** For interacting with OpenAI's GPT models.
- **python-dotenv:** For loading environment variables from `.env`.
- **os:** For environment variable access.
- **dotenv:** For loading `.env` file.
- **Custom modules:**  
  - `controller_agent.py`: Orchestrates agent interactions.
  - `specialized_agents/research_agent.py`: Handles research tasks.
  - `specialized_agents/summarization_agent.py`: Handles summarization tasks.
  - `tools/web_search_tool.py`: Integrates SerpAPI.
  - `tools/summarizer_tool.py`: Integrates OpenAI API.
  - `tools/output_formatting_tool.py`: Formats output for display.
  - `tools/custom_domain_extractor.py`: Custom tool for extracting domain-specific information.

### Environment Variables
```
OPENAI_API_KEY=your-openai-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```
- **Purpose:** Keeps sensitive API keys out of the codebase and version control.

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

### CLI (if using `main.py`)

- Follow the prompts to choose between research and summarization.

---

## Agent & Tool Descriptions

### ControllerAgent
- Orchestrates tasks and delegates to the appropriate agent.
- Implements error handling and fallback mechanisms.
- Maintains a registry of specialized agents.
- Communication protocol for agent collaboration.

### ResearchAgent
- Handles research queries.
- Uses:
  - **WebSearchTool:** Fetches search results from SerpAPI.
  - **SummarizerTool:** (Optional) Summarizes results if needed.
  - **CustomDomainExtractor:** Extracts domain-specific information.
- Maintains context for each query.

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
- **Enhancement:** Makes research output more relevant and actionable.
- **Error Handling:** Handles missing or malformed data gracefully.

---

## Orchestration System

- **Workflow:**  
  The ControllerAgent receives tasks from the UI and delegates them to the appropriate specialized agent.
- **Task Execution:**  
  Sequential execution for research and summarization tasks.
- **Memory Management:**  
  Each agent maintains context for improved coherence.
- **Error Handling:**  
  Robust error handling for API failures and missing data.
- **Feedback Loops:**  
  (Planned) For agent improvement and reinforcement learning.

---

## Evaluation

### Test Cases

- Research queries on various topics (e.g., "best AI models", "Claude vs GPT").
- Summarization of long and short texts.
- Edge cases: empty input, API failure, malformed data.

### Metrics

- **Accuracy:** Relevance of search results and summaries.
- **Efficiency:** Response time for each task.
- **Reliability:** Robustness to API errors and missing data.
- **User Experience:** Clarity and helpfulness of output.

### Results

- System meets stated objectives for research and summarization.
- Handles edge cases and maintains context across interactions.
- Responsive and user-friendly web interface.

---

## Challenges & Solutions

- **API quota management:** Handled by using environment variables and error handling.
- **Result formatting:** Used a dedicated formatting tool for clean UI.
- **Extensibility:** Modular design for easy addition of new features.
- **Context management:** Each agent maintains its own memory for coherence.

---

## Limitations & Future Work

- **Web search limited by SerpAPI quota and coverage.**
- **Summarization limited by OpenAI API quota.**
- **Future:** Add more agents, support more domains, improve extraction logic, and add feedback loops for agent improvement.

---

## License

MIT License

Copyright (c) 2025 Sanat Popli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Acknowledgements/Contributions

- [OpenAI](https://openai.com/)
- [SerpAPI](https://serpapi.com/)
- [Streamlit](https://streamlit.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

*For any questions, please contact popli.sa@northeastern.edu*
