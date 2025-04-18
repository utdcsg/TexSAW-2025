.PHONY = build

build:
	python obfuscate_chal.py plaintext_chal.py > chal.py
	python -m dis chal.py > chal.txt

clean:
	rm ./chal.py ./chal.txt
	rm -rf ./__pycache__
	
