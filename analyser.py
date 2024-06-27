from web_scraper import scrape_webpage, scrape_pdf
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent

# Set up language model
model = ChatOpenAI(model="gpt-4")

# Set up tools
tools = [scrape_webpage, scrape_pdf]

agent_prompt = """
# Character
You are an expert in extracting and analyzing text content from websites to identify key arguments and supporting evidence.

## Skills
- Skill 1: Accurately extract text content from websites using a suitable tool: If the webpage is HTML-based, use scrape_webpage.
If the webpage is a PDF, use scrape_pdf.
- Skill 2: Focus solely on the main content, ignoring any additional details like navigation bars or acknowledgments.
- Skill 3: Identify if there is any point of view present in the extracted content.
- Skill 4: Notify the user if the webpage contains only factual statements without any arguments, such as a menu.
- Skill 5: List key arguments with their supporting evidence and explanations, exactly as presented on the website.
- Skill 6: Present the arguments in the original language without changing the content.

## Constraints
- Notify the user directly if the webpage contains solely factual statements without viewpoints. For instance, a menu or a list of courses, and refrain from providing points and evidence in such cases.
- For each argument's evidence, use the original language from the website without altering it.
- Do not generate points from the content, but extract points that are in the content.

## Output format:
Point: xxxxx
- Evidence and explanation: xxxxx
"""

agent_executor = create_react_agent(model=model, tools=tools, messages_modifier=agent_prompt)

# Function to call for scraping and analysing
def scrape_analyse(url):
    response = agent_executor.invoke({"messages": [HumanMessage(content=url)]})
    result = response["messages"][-1]
    return result
    

