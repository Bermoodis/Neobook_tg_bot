import telebot
from telebot import types

# Создание экземпляра бота
bot = telebot.TeleBot('6263911640:AAEi3PZ4w_lRR2hOZPsJQi6vrKjS6mafPw0')


# Функция, которая обрабатывает команду старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # Reply - шаблоны, не привязанные к какому-либо сообщению юзера
    project_btn = types.KeyboardButton("📄 О проекте")
    contact_btn = types.KeyboardButton("📩 Связаться с админом")
    site_btn = types.KeyboardButton("🔗 Перейти на сайт")
    menu_btn = types.KeyboardButton("🗃 Меню")
    markup.add(project_btn, contact_btn, site_btn, menu_btn)
    # Отправка сообщения, после нажатия "start"
    bot.send_message(message.from_user.id,
                     "Привет!\nДавай я покажу тебе, что умею делать.\nПросто ткни пальцем на любую кнопку.",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # О проекте
    if message.text == '📄 О проекте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_return_btn = types.KeyboardButton(' Вернуться в главное меню')
        markup.add(menu_return_btn)
        bot.send_message(message.from_user.id,
                         'Прочитать подробнее о моей истории создания и функциях можно здесь: '
                         + '[Жмякай сюда](https://telegra.ph/Bot-Karmannyj-Neo-03-13)', reply_markup=markup,
                         parse_mode='Markdown')
    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        project_btn = types.KeyboardButton("📄 О проекте")
        contact_btn = types.KeyboardButton("📩 Связаться с админом")
        site_btn = types.KeyboardButton("🔗 Перейти на сайт")
        menu_btn = types.KeyboardButton("🗃 Меню")
        markup.add(project_btn, contact_btn, site_btn, menu_btn)
        bot.send_message(message.from_user.id, 'Ты вернулся в самое главное меню\n Жмякай на новую кнопку скорее',
                         reply_markup=markup)

    elif message.text == '📩 Связаться с админом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_return_btn = types.KeyboardButton(' Вернуться в главное меню')
        markup.add(menu_return_btn)
        bot.send_message(message.from_user.id,
                         'Напиши главному админу, какой он плохой.\nИли поделись впечатлениями о боте и своими идеями ' + '\n[Жмякай сюда](nespletnik@gmail.com)',
                         reply_markup=markup,
                         parse_mode='Markdown')

    elif message.text == '🗃 Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contest_btn = types.KeyboardButton("⚔️ Конкурсы Neo")
        books_btn = types.KeyboardButton("📚 Книга вслепую")
        author_btn = types.KeyboardButton("📚👨‍🏫 Рандомный автор")
        markup.add(contest_btn, books_btn, author_btn)
        bot.send_message(message.from_user.id,
                         'Смотри, что теперь я могу предложить', reply_markup=markup,
                         parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)
