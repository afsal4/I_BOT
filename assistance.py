from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, SystemMessage, HumanMessage

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser 
import os

os.environ["OPENAI_API_KEY"] = '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'

history = ''''''

chat = ChatOpenAI()

job_description = """the job should consist of machine learning question we are looking for a candidate with the basics knowledge on machine learnin"""



chat = ChatOpenAI()




messages_history = [
    SystemMessage(content=f"""you are a job interviewer and your job is to interview candidate according to company's need
                  
                  Company's job description: {job_description}
                  
                  things that you should ask only after the human response which we will provide shortly(Note you should not ask all at once only ask them one by one after humans response):
                  (
                    welcome the candidate ,
                    Ask some common interview questions ,
                    Ask job related questions,
                    Ask questions related to answers,
                    score the answers according to each of his/her reply ,
                    you should always ask one question at a time and wait for his/her reply and ask again,
                    say the conclusion and finish the interview it should consist of a string conclusion 
                   )
                  """), 
    
        SystemMessage(content="""
                      Rules that should not be broken while having a conversation:
                      (
                          dont ask questions repeatedly,
                          no questions for other jobs,
                          ask questions one by one only after HumanMessage,
                          should not give the job if the person is speaking illmannered, 
                          should give the candidate a score based on these rules and also his performance at the end,
                          )
                          
                        These rules are strict and should not be broken
                        """)
]


for i in range(20):
    ai = chat(messages=messages_history).content
    print(ai)

    chats = input('your chats: ')
    messages_history.append(AIMessage(chats))
    
    messages_history.append(HumanMessage(chats))
    



