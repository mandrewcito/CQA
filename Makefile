LANG = python
APP = main.py

all: run

run:
	@$(LANG) $(APP) 

clean:
	@find . -name "*.pyc" -exec rm -f '{}' +
	@find . -name "*~" -exec rm -f '{}' +
	@echo "Done!"

logo:
	@cat logo.txt
