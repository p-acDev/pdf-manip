# pdf-manip
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pacourbet/pdf-manip?display_name=tag&style=plastic)
![Lines of code](https://img.shields.io/tokei/lines/github/pacourbet/pdf-manip?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pacourbet/pdf-manip?style=plastic)

# Installation

Il faut juste executer la commande:

`pip install -r requirements.txt`

## Problème avec `PyQt5` sur mac os puce M1

Il faut installer PyQt5 avec brew puis ajouter au path les chemins

```
brew install pyqt5
echo 'export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="/opt/homebrew/opt/pyqt@5/5.15.4_1/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

et ensuite faire:

`pip install pyqt5`

:point_right: https://stackoverflow.com/a/70296259/14823310

## OCR 
à ajouter sur windows si app en local
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
