import os 
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType

os.environ["OPENAI_API_KEY"] = "set_api"


def scoring(question, answer, job_description):
    """
    7 or above 7 answered correctly
    5 or above 5 answered but need to improve 
    3 or above 3 some knowledge about it but dont know the answer
    0 or above 0 dont know the answer
    """
    
    
    llm = OpenAI(temperature=.5)

    
    template_2 =  """
    you are an scoring partner for interview questions for a company:
    
    the question that is asked would and the answer are given 

    you should score this out of 10:
    scores should be between 1 to 10
    7 or above 7 answered correctly
    5 or above 5 answered but need to improve 
    3 or above 3 some knowledge about it but dont know the answer
    0 or above 0 dont know the answer

    
    score based on: 
    * creativity 
    * honesty
    * accuracy of answers 
    * manners
    * indepth knowledge 
    * projects
    * if the question doesnt have any importance answers doesnt matter so give points for that
    
    should reduce the points:
    * unappropriate behaviour 
    * dont know the answers
    * not giving proper answer
    * not speaking proper english
    
    
    Company Job description: {job_description}
    
    Question: {question}

    Answer: {answer}
    
    Company Job description is the criteria given by the company for hiring candidates
    
    Question is the question asked by the interviewer
    
    Answer is the answer given by the candidate
    
    Only return the score no need of any description should only answer in digits and nothing else
    Only in this format and nothing else:
    
    Score: ..
    
    """
    
    
    # template for scoring
    prompt = PromptTemplate(
        input_variables=['question', 'answer', 'job_description'],
        template=template_2
    )
    
    # chaining the model and the template 
    chain = LLMChain(llm=llm, prompt=prompt, output_key='score')
    
    # response from the llm model 
    response = chain.invoke({'question': question, 'job_description': job_description, 'answer': answer})
    
    # cleaning the score output from llm
    score = response['score'].strip()
    score = [i for i in score if i.isdigit()][0]
    
    return int(score)


def resume_scoring():
        

    
    template_1 = """
    you are an scoring partner for interview questions:
    
    the score would be based on the following details:
    * resume
    * performance during the interview
    * proper behaviour 
    * knowledge for the company job description
    * creativity 
    * projects 

    you should score this out of 100 
    above 70 means passed 
    above 50 means consideration
    50 and below failed 
    
    """


# question = "what is your name"
# answer = "my name is afsal"


question = "what is machine learning"
answer = 'machine learning is a technique used for predicting data from the data that it has trained. it is used in object detection, stock prediction and etc'
job_description = 'we are looking for a machine learning fresher who has indepth knowledge in python'

for i in range(10):

    print(scoring(question, answer, job_description))