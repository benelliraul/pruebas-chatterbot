from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging 
from chatterbot.response_selection import get_most_frequent_response

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)
chatbot = ChatBot("Ejemplo de bot", read_only=True)
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train(
#    './preguntas_varias.yml'
#)
usuario = " "

while usuario != "exit":
    usuario = input (">>>")

    if usuario != 'exit':
        
        respuesta = chatbot.get_response(usuario)
        print ("BOT: " +str(respuesta))
