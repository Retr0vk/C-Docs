import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json
from vk_api import VkApi
from datetime import datetime
from datetime import timedelta
import timeit

session = vk_api.VkApi(token='8074b2aa1d5586ca23e4fbe3c3ab2d3746ca16711ca86031379fad102765ab2766b19e1227b30cf6e52dc')
vk = session.get_api()
longpoll = VkLongPoll(session)

flags = {
    "user_join": 6,
    "user_kick": 8
}

chat_ids = [561, 289]


def messages_send(message):
    vk.messages.send(chat_id=event.chat_id, message=message, random_id=get_random_id())


data = json.load(open("users.json", "a+"))


try:

    for event in longpoll.listen():

        if event.from_chat and event.chat_id in chat_ids:

            if event.type_id == flags["user_join"]:
                user_id = event.info["user_id"]
                hello_message = "Добро пожаловать в беседу VIP продавцов BLACK GTA SHOP.\n\n" \
                                "ПРАВИЛА:\n" \
                                "1.Оскорбления запрещены.\n2.Срачи не приветствуются.\n3.Разрешено свободное общение.\n4.Запрещена реклама сторонних торговых площадок.\n\n" \
                                "За нарушения данных правил вы будете лишены VIP статуса, получите отказ в выводе средств " \
                                "и будете исключены из этой беседы. "
                messages_send(message=hello_message)

            if event.type_id == flags["user_kick"]:
                user_id = event.info["user_id"]
                print("Kick User!")

except:
    pass
