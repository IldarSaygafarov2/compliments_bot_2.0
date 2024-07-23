from data.loader import bot
import handlers
from handlers.commands import send_compliment_by_me
import threading
import schedule


def schedule_func():
    schedule.every(5).hours.do(send_compliment_by_me)
    while True:
        # time.sleep(10)
        schedule.run_pending()




if __name__ == '__main__':
    print('bot started')
    try:
        bot.infinity_polling()
        threading.Thread(target=schedule_func).start()
    except KeyboardInterrupt:
        print('bot stopped')
        threading.Event().clear()
    