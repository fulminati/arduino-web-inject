
install:
	@pip3 install -r requirements.txt

version:
	@grep '__version__ =' arduino_web_inject.py | sed -r 's/.*([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*)[^0-9]*/\1/'

bump-version:
	@echo $$(make -s version | cut -d. -f1).$$(make -s version | cut -d. -f2).$$(($$(make -s version | cut -d. -f3)+1))
	
pip:
	@pip3 install --upgrade pip setuptools wheel
	@pip3 install tqdm
	@pip3 install --user --upgrade twine

release: 
	@sed -i "s/__version__ =.*/__version__ = '$$(make -s bump-version)'/" arduino_web_inject.py
	@git add .
	@git commit -am "Release"
	@git push
	@rm -rf build/ dist/ *egg* **.pyc __pycache__
	@python3 setup.py bdist_wheel --universal
	@python3 -m twine upload dist/*

test:
	@python3 inject.py
