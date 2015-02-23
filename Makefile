LANG = python
APP = main.py

all: run logo

install:
	@echo "instalar/configurar couchDB"
	@echo "cofigurar crontab"
	@echo "instalar dependencias librerias graficas"

run:
	@$(LANG) $(APP) 

clean:
	@find . -name "*.pyc" -exec rm -f '{}' +
	@find . -name "*~" -exec rm -f '{}' +
	@echo "Done!"

logo:
	@cat logo.txt
