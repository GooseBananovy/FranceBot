AUTH_ASK = 'Катька принцесска?🌚'


DIALOGUE_PROMPT = '''
RÔLE: vous êtes Anna, une interlocutrice sympathique et patiente, parlant français au niveau A1/A2, pratique pour les débutants. Utilisez un vocabulaire simple et une grammaire de base, en se concentrant sur les sujets quotidiens et les intérêts de l'utilisateur. 

OBJECTIF: mener un dialogue vivant et naturel, poser des questions ouvertes, stimuler l'utilisateur à parler de lui-même, de ses passe-temps et de ses expériences. Répondez aux questions en expliquant les nouveaux mots avec des exemples simples, corrigez doucement les erreurs par reformulation ou clarification des questions, évitez les critiques directes. Chaque message est limité à 2-3 phrases pour maintenir la dynamique. Utilisez pas plus d'un smiley, en les changeant pour la vivacité de la communication. Inclure des nuances culturelles et des phrases utiles pour plonger dans la culture française et améliorer la compréhension de la langue.

EXEMPLE DE DIALOGUE: 
Assistant: Salut! Comment tu te sens aujourd'hui? 😊 
User: Bonjour! Je me sens bien. Aujourd'hui j’ai été en visite chez un ami. 
Assistant: C’est super! Ton ami habite près de chez toi? 
User: Non, mon amie vit assez loin. J'ai dû aller dans une autre ville en bus. 
Assistant: Très intéressant. Le trajet en bus était comment? 

FORMAT de RÉPONSE: français Naturel, convivial et simple, comme dans un support de niveau A1/A2, avec des corrections douces et des insertions culturelles. Tous vos mots doivent être exclusivement en français.

NOTE: Ne pas expliquer leurs actions, ou leurs objectifs, il suffit de communiquer directement, ne pas rendre compte
'''


DIALOGUE_START_MESS = '''
🎉 Bienvenue в режиме диалога!💬

Теперь ты можешь свободно общаться на французском — будто сидишь в уютном парижском кафе!☕
Я буду твоим собеседником: отвечу, задам вопросы и помогу погрузиться в язык.

🛠️ Доступные команды:
/dial 🔄 — Начать новый диалог
/trans 🌍 — Перевести твоё следующее сообщение
/translst 📖 — Перевести мой последний ответ
/stop 🚪 — Выйти из режима (но мы будем скучать!😢)

Говори смело — ошибки это ступеньки к Maîtrise!🚀
'''


WELCOME_MESS = '''
🇫🇷 Bonjour, друг!🐱

Этот бот — твой лучший помощник в изучении французского языка!
Пока он ещё учится сам, поэтому иногда может ошибаться.
Если заметишь баг, сообщи создателю, и мы вместе сделаем его лучше!💙

🔒 Для старта нужна авторизация:
Просто напиши /auth и ответь на простой вопрос!🥐

ℹ️ Все команды под рукой:
Нажми /info — и увидишь список начальных команд!📜

Погружайся в язык с удовольствием!🌟
'''


HELP_MESS = '''
/start 🚀 - Информация о проекте
/auth 🔐 - Авторизация
/dial 💬 - Войти в режим диалога
/stop 🚪 - Выйти из режима
/trans 🌍 - Перевести твое следующее сообщение
/info 📋 - Показать список команд
'''


UNKNOWN_COMM = '''
Неизвестная команда!😨
Используй /info чтобы ознакомиться со списком команд
'''


MISS_MODE = '''
Для начала выбери режим!😡
Используй /info чтобы ознакомиться со списком команд.
'''


STOP_MESS = 'Режим "{}" был остановлен.'


MISS_AUTH = '''
Ты не авторизован(а)!😡
Используй /auth для авторизации.
'''
ALR_AUTH = 'Ты уже авторизован(а)😇'


SWITCH_MESS = 'Режим "{}" был переключен на "{}".'


COR_PASSW = 'Пароль принят!😇'
INCOR_PASSW = '''
Пароль неверный😡
Попробуй еще раз!
'''


RESET_MESS = 'Режим "{}" был перезапущен.'

STICKER_ID = 'CAACAgIAAxkBAAEBeo5og5uyYrVLyekWkyHDs44U_-ROAgACTiwAAqNE6ErPBKpc548ETzYE'

URL = 'http://localhost:5000/translate'

MISS_MESS_FROM_BOT = 'Сначала дождись сообщения от собеседника!😡'

UNKNOWN_ERR = '''
Неизвестная ошибка!☠️
Пожалуйста сообщи создателю.
'''

TRANS_MESS = '''
Твое следующее сообщение будет переведено😇
'''

DIAL_BUTTONS = [['/dial', '/stop'],['/trans', '/translst']]