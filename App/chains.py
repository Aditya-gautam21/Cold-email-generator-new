import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()



class Chain:
    def __init__(self):
        self.llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", groq_api_key=os.getenv('GROQ_API_KEY'), temperature=0)

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
        ### SCRAPPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scrapped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing following keys: 'role','experience','skills' and 'description'.
        Only return the valid JSON
        ### VALID JSON(NO PREAMBLE)
        """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
          json_parser = JsonOutputParser()
          res = json_parser.parse(res.content)

        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")

        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            '''
        ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
         You are Aditya, a 3rd year BTech. undergraduate, branch cse(aiml). You are looking for a paid internship in the field of Artificial Intelligence and machine learning and related fields such as data science and data analytics.
         Your job is to write a cold email to the companies regarding the job mentioned above describing my capabilities in fulfilling their needs.
         Remember you are Aditya, btech undergraduate, 3rd year. 
         Do not provide a preamble.
         ### EMAIL (NO PREAMBLE):
        '''
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({'job_description': str(job), 'link_list': links})
        return res.content