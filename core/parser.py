
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def parse_output(response):
    parser = JsonOutputParser()
    
    try:
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse LLM output")