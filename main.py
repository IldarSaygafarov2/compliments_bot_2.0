from data.loader import bot
import handlers
from handlers.commands import send_compliment_by_me
import threading
import schedule
import time


# def schedule_func():
#     schedule.every(10).seconds.do(send_compliment_by_me)
#     while True:
#         time.sleep(1)
#         schedule.run_pending()


if __name__ == '__main__':
    print('bot started')
    try:
        # threading.Thread(target=schedule_func).start()
        bot.infinity_polling()
    except KeyboardInterrupt:
        print('bot stopped')
        # threading.Event().clear()
    