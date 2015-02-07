LANG = python

all: compile run

compile:
	@echo "working on it "

run:
	@echo "be patient :)"

clean:
	@find . -name "*.pyc" -exec rm -f '{}' +
	@find . -name "*~" -exec rm -f '{}' +
	@echo "Done!"

logo:
	@cat logo.txt
