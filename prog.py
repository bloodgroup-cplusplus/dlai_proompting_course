import openai 
import os 

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


openai.api_key = "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"




def get_completion (prompt, model = "gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model = model, 
        messages = messages, 
        temperature = 0,
        max_tokens= 20
        )
    return response.choices[0].message["content"]




if __name__ == "__main__":

    # Prompting Principles 
    # Principle 1: Write cleear and Specific Instructions 
    # Principle 2 : Give the modle time to "think " 

    # Tactics 
    # Tactic 1 : Use delimiters to clearly indicate distinct parts of input 


    # dElimiters can by anything like ```, """, <> <tag> </tag> , : 

    text = f"""
    You should express what you want to model to do by \
    providing instructions that are as clear and \
    specific as you can possibly make them. \ 
    This will guide the model towards the desired output, \ 
    and reduce the chances of receiving irrelevant \ 
    or incorrect responses. Don't confuse writing a \ 
    clear prompt with writing a short prompt. \ 
    In many cases, longer prompts provide more clarity \ 
    and context for the model, which can lead to \ 
    more detailed and relevant outputs.
    """

    prompt = f"""
    Summarize the text delimited by triple backticks into a single sentence . 
    ``` {text} ``` 
    """

    response = get_completion(prompt)
    print(response)

