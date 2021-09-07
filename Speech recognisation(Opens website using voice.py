import speech_recognition as sr
import webbrowser as web



def main():
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"

r=sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Search Your Query")

    audio = r.listen(source)

    print("Reconizing Now ... ")
try:
            search = r.recognize_google(audio)
            print("You have said : " + search)
            web.register('chrome',
                                None,
                                web.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            web.get('chrome').open(search)



except sr.RequestError as e:

    print("Could not request results; {0}".format(e))


except sr.UnknownValueError:

    print("unknown error occured")
if __name__ == "__main__":
 main()