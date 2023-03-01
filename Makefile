
install:
	@pip3 install -r requirements.txt

version:
	@grep '__version__ =' arduino_web_inject/main.py | sed -r 's/.*([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*)[^0-9]*/\1/'

next-version:
	@echo $$(make -s version | cut -d. -f1).$$(make -s version | cut -d. -f2).$$(($$(make -s version | cut -d. -f3)+1))

bump-version:
	@sed -i "s/__version__ =.*/__version__ = '$$(make -s next-version)'/" arduino_web_inject/main.py

pip:
	@pip3 install --upgrade pip setuptools wheel
	@pip3 install tqdm pytest
	@pip3 install --user --upgrade twine

push:
	@git add .
	@git commit -am "Release"
	@git push

check: 
	@twine check dist/*

release: bump-version push
	@rm -rf build/ dist/ *egg* **.pyc __pycache__
	@python3 setup.py bdist_wheel --universal
	@python3 -m twine upload dist/*

test:
	@python3 arduino_web_inject/main.py tests/fixtures

test-fixtures:
	@clear
	@python3 arduino_web_inject/main.py tests/fixtures

test-not-args:
	@python3 arduino_web_inject/main.py

test-not-a-dir:
	@python3 arduino_web_inject/main.py tests/this-is-not-a-dir

test-examples:
	@python3 arduino_web_inject/main.py examples

test-server:
	@python3 arduino_web_inject/server.py examples

test-minify-html:
	@clear
	#@pytest -s arduino_web_inject/tests/minify_html_test.py
	@python arduino_web_inject/tests/minify_html_test.py 