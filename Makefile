
install:
	@pip3 install -r requirements.txt

pip:
	@pip3 install --upgrade pip setuptools wheel
	@pip3 install tqdm
	@pip3 install --user --upgrade twine

release: pip
	@git add .
	@git commit -am "Release"
	@git push
	@rm -rf build/ dist/ *egg* **.pyc __pycache__
	@python3 setup.py bdist_wheel --universal
	@python3 -m twine upload dist/*

test:
	@python3 inject.py
