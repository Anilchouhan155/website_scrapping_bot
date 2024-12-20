import requests
from bs4 import BeautifulSoup
from config import OPENAI_API_KEY
from models import WebsiteDetails
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


# openai.api_key = OPENAI_API_KEY

# Function to preprocess the head content
def extract_page_text(html_content: str) -> str:
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and return only the text content
    page_text = soup.get_text(separator="\n")  # Use a separator for better readability
    return page_text.strip()


# Define the response schema
response_schemas = [
    ResponseSchema(name="industry", description="The industry of the company or 'not mentioned'"),
    ResponseSchema(name="company_size", description="The size of the company (small, medium, large, or 'not mentioned')"),
    ResponseSchema(name="company_location", description="The location of the company or 'not mentioned'"),
]

# Use LangChain's structured output parser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Create the prompt with validation
prompt = PromptTemplate(
    template="""
    Using the following website content, answer these questions:
    1. What industry does the company belong to?
    2. What is the size of the company (small, medium, large)?
    3. Where is the company located?

    Page Content:
    {page_content}

    Respond with a strict JSON object containing:
    {response_format}
    """,
    input_variables=["page_content"],
    partial_variables={"response_format": output_parser.get_format_instructions()},
)

# Use LangChain to process the request
def extract_details_with_langchain(url: str):
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)  # Use temperature=0 for deterministic responses

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL: {response.status_code}")

    # Preprocess the page content
    page_content = extract_page_text(response.text)

    formatted_prompt = prompt.format_prompt(page_content=page_content)
    response = model(formatted_prompt.to_string())
    return output_parser.parse(response.content)