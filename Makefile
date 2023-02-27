
install:
	@pip3 install -r requirements.txt

release:
	@git add .
	@git commit -am "Release"
	@git push

test:
	@python3 arduino-web-inject.py
