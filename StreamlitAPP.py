#importing the libraries
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os
import json
import pandas as pd 
import traceback

from src.mcqgenrator.utils import read_file, get_table_data
from src.mcqgenrator.MCQGenerator import generate_evaluate_chain
from src.mcqgenrator.logger import logging
import streamlit as st


#loading the json file 
# with open("D:\work\projects\project_ChatBot\resopnse.json" , 'r') as file:
#     RESPONSE_JSON=json.loads(file)
file = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
    "2": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
    "3": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
}
#creating the tile of the app
st.title("Mcq generation app using langchain")

#creating a form for the user
with st.form("user input"):
    #file uplad
    uploaded_file=st.file_uploader("uploaded as a pdf file ")

    #input field
    mcq_count=st.number_input("no of mcq", min_value=3, max_value=50)

    #subject
    subject=st.text_input("insert subject",max_chars=20)

    #quiz tone
    tone=st.text_input("complexity level of the question", max_chars=20, placeholder="Simple")
    
    #add the button 
    button=st.form_submit_button("generate the mcq")

    #checking if the button is clicked
    
    if button and uploaded_file is  not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try :
                text=read_file(uploaded_file)
                #count token and the cost of api call
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                    {
                    "text": text,
                    "number": mcq_count,
                    "subject":subject,
                    "tone": tone,
                    "response_json": json.dumps(file)
                    })
            except Exception as e:
                # traceback.print_exception(type(e), e, e.__trackback__)
                st.error("error")
                
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    #extracting the quiz data
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #display review in the box
                            st.text_area(label="review", value=response["review"])
                        else:
                            st.error("error in the table data")
                else:
                    st.write(response)
                        
        
                