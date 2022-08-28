import os
import random
import speech_recognition
import webbrowser
import pyautogui
import time

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


commands_dict = {
    'commands': {
    'welcome': ['привет', 'здарова'],
    'open_youtube': ['открой ютуб', 'запусти ютуб'],
    'yes_i_m_too_good': ['да вроде более или менее', 'да все более или менее', 'вроде нормально всё', 'более или менее','всё нормально', 'нормально', 'хорошо', 'всё хорошо'],
    'open_dota': ['запусти доту', 'открой доту'],
    'i_m_dont_too_good': ['ну такое', 'ну такое себе', 'такое себе', 'бывало и лучше'],
    'funcional': ['что ты умеешь', 'что ты можешь'],
    'open_browser': ['открой браузер', 'запусти браузер'],
    'random_number': ['рандомное число'],
    'open_vk': ['открой вконтакте'],
    'open_vk_music': ['плейлист', 'включи музыку', 'мой плейлист', 'музыка'],
    }
}

while True:
    def commands_bot():
        try:
            with speech_recognition.Microphone() as micro:
                sr.adjust_for_ambient_noise(source = micro, duration = 0.5)
                audio = sr.listen(source=micro)
                query = sr.recognize_google(audio_data=audio, language= 'ru-RU').lower()
            return query
        except speech_recognition.UnknownValueError:
            return 'Я не понял что ты сказал...'


    def funcional():
        return 'Я могу открыть доту на твоем компухтере.\nМогу открыть ютуб, либо браузер, в зависимости от того, что ты попросишь.\nА также включить плейлист в вк, какой попросишь.'

    def welcome():
        return ('Здорова, хлопец)\nКак дела твои?')

    def open_dota():
        print('Секунду...')
        return os.startfile(r'C:\Users\Илья\PycharmProjects\Project1\Dota 2.url', 'open')

    def yes_i_m_too_good():
        return ('Ну и славненько)')

    def i_m_dont_too_good():
        return 'Не расстраивайся, все, что ни делаетя, все к лучшему)'

    def random_number():
        return 'Твое число: ' + str(random.randint(1,10000))

    def open_vk():
        print('Секунду...')
        return webbrowser.open('https://vk.com/feed')

    def open_vk_music():
        print('Секунду...')
        webbrowser.open('https://vk.com/audios286431422?section=all&z=audio_playlist478520856_30')
        time.sleep(4)
        x = pyautogui.locateOnScreen('Перемешать.PNG')
        pyautogui.click(x)
        return 'Успешно!'

    def open_youtube():
        print('Секунду...')
        return webbrowser.open('https://www.youtube.com/')

    def open_browser():
        print('Открываю...')
        return webbrowser.open('https://www.google.com/firefox/')

    def main():
        query = commands_bot()
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())

    if __name__ == '__main__':
        main()