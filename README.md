clone le repo 
```
git clone https://github.com/Clamcloum/ollama-webchat.git
```

créer environnement virtuel et l'activer ( windows )
```
py -m venv venv
.\venv\Scripts\Activate.ps1
```
autoriser l'execution de script powershell ( Windows )
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

sur linux
```
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
