# Chatbot
## Über dieses Projekt
Dieses Projekt entstand für das Modul "Grundlagen der KI" und implementiert zwei verschiedene Chatbots mit dem [Program Y Framework](https://github.com/keiffster/program-y). Es handelt sich hierbei um ein pythonbasiertes AIML 2.0 Framework mit vielen Schnittstellen zu Services wie Discord, Alexa, etc. .

## Installation
1.Clone Repository
2.Terminal im Ordner program-y öffnen.
"source ./bin/activate" im Terminal eingeben und bestätigen. (Virtual Environment wird geladen)
Im Virtual environment, welches sich eben gestartet haben sind alle Module vorinstalliert, somit ist der Bot ready to run.

## Easybot: [Webchat](http://195.62.33.141:8090/)
Easybot ist ein simpler Bot der leichten Smalltalk halten kann. Die Dateien für den Easybot können im Directory [Easybot](https://github.com/jsbn60-sys/Chatbot/tree/main/programy/Easybot) gefunden werden. Spezieller noch können die .aiml-Dateien des Bots [hier](https://github.com/jsbn60-sys/Chatbot/tree/main/programy/Easybot/storage/categories) gefunden werden.
Wir empfehlen mit Easybot über den Webchat zu interargieren. Lokal kann Easybot ausgeführt werden indem zu cd Easybot/scripts/xnix/ navigiert wird, dort "./template-y.sh" eingeben und Ausführen.
Zudem haben wir bereits alles am Webserver umkonfiguriert, sodass er lokal laufen kann, lediglich "./template-webchat.sh" muss per Terminal aufgerufen werden.
Zum nutzen der TTS-Funktion rufen sie den Webadresse mit Firefox oder Chrome auf und klicken sie nach einer Nachricht auf den Lautsprecher, welcher oben Rechts platziert ist.

## THM-Bot:
Der THM-Bot beantwortet Fragen rund um das Thema Studium an der THM. Er fokussiert sich hauptsächlich auf die Informatik. Wir empfehlen es nicht zu versuchen, Support-Bot lokal laufen zu lassen, sondern mit ihm über den oben verlinkten Discord-Server zu sprechen. Die Dateien für Support-Bot können im Directory [THM-Bot](https://github.com/jsbn60-sys/programy/THM-BOT) gefunden werden. Spezieller noch können die .aiml-Dateien des Bots [hier](https://github.com/jsbn60-sys/programy/THM-BOT/tree/main/THM-Bot/storage/categories) gefunden werden.
Um mit dem THM-Bot zu kommunizieren navigieren sie zu THM-Bot/scripts/xnix und führen dort "./THM-bot.sh" aus.
Um den Discord Bot zu starten, starten sie bitte den sanic Client mit dem Befehl "python3 -m programy.clients.restful.sanic.client --config ../config/xnix/config.sanic.rest.yaml --cformat yaml --logging ./logging.y"
Anschließend führen sie den Discord-Bot mit "python3 DBot.py" aus, beachten sie, dass sie einen eigenen Token generieren müssen, welche in DBot.py geändert werden muss.
Um mit dem Bot ohne setup direkt über Discord zu sprechen können sie auch auf den von uns konfigurierten Server joinen: https://discord.gg/egYgAscxFX
Fürs Ausführen von TextToSpeech starten sie erneut wie oben beschrieben den sanic Client und starten sie anschließend "python3 TextToSpeech.py"

## Parser:
Um den Parser zu starten, führen sie im Verzeichnis "programy" im Terminal den Befehl "python3 Parser.py" aus.
Um einen anderen Studiengang zu parsen, ändern sie den letzten Link im File.

### Entwickler: Marius Butteron, Bright Baah, John Beinecke
