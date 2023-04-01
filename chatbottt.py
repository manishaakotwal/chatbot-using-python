from nltk.chat.util import Chat,reflections
pairs = [
    [r'hi',['hiii']],
    [r'hii|hello|heyy',["hii there"]],
    [r'whats your name?',['I am a chatbot.I try to answer questions']],
    [r'where are you from',['I am from INDIA']],
    [r'how are you',['I am good,how about you?']],
    [r'who designed you',['I am designed by manisha']],
    [r'what kind of work do you do? ',['I work in Software.. and as a conversational application.']],
    [r'give one sentense about python?',['Python is a simple programming language']],
    [r'What is AI',['Artificial Intelligence is the branch of engineering and science devoted to constructing machine thats think...']],
    [r'ok Byeee!!',['Byeee ,have a nice day']]

]
chat = Chat(pairs,reflections)
chat.converse()
def quit():
    print("Hii I am chatbot.Ask me something")
if __name__=="__main__":
    quit()