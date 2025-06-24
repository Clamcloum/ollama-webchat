❌necessite d'heberger Ollama en local❌

clone le repo 
```
git clone https://github.com/Clamcloum/ollama-webchat.git
```


autoriser l'execution de script powershell ( Windows )
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```


créer environnement virtuel et l'activer ( windows )
```
py -m venv venv
.\venv\Scripts\Activate.ps1
```


sur linux
```
python3 -m venv venv
source venv/bin/activate
```


Installer les packages
```
pip install -r .\requirements.txt
```


Pour lancer son app 
sur windows
```
py app.py
```
Sur linux
```
python3 app.py
```
