# Scraper + Argument Identifier

This is an AI agent that can extract text information from a given website and identify, if any, the points of argument in the content of the website, then return a list of arguments and their corresponding evidence and explanation.

----------
## Test on Coze (no workflow)
**Prompt used:** see [Sample Prompt 01](Sample_Prompt_01.md).

**Plugins used:**
- Browser / browse
- PDF Tools / read_pdf

**Link to the bot:** https://www.coze.com/store/bot/7384373288149188613?bot_id=true

## Test on Coze (with workflow)
**Prompt used:** shortened version of [Sample Prompt 01](Sample_Prompt_01.md), with the following lines added at the end: <br>
The content to be analysed is {{content_webpage}}. If {{content_webpage}} is empty, analyse {{content_pdf}} instead. <br>
Where {{content_webpage}} are {{content_pdf}} are extracted using the plugins.


**Plugins used:** 
- Browser / browse
- PDF Tools / read_pdf

**Workflow:** 
Start &#8594; *browse_raw* &#8594; 
- if content of *browse_raw* not empty proceed to LLM
- else use *read_pdf* to extract content instead and pass to LLM

**Link to the bot:** https://www.coze.com/store/bot/7384484733989781509?bot_id=true


## Python implementations
The agent was built with LangChain function create_react_agent.  It is equipped with two tools to choose between and utilise for extracting text, namely *scrape_webpage* and *scrape_pdf*, depending on the feature of the webpage. 
<br>After the extraction the agent will analyse the extracted text and produce a list of points and evidence if there are any present, returned as an *AIMessage* object which was imported from LangChain.
<br> To run the agent, please call the function *scrape_analyse*.


## Urls for tests
You can find the urls used for test here: [Test urls](Test_urls.md).