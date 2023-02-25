

release:
	@git add .
	@git commit -am "Release"
	@git push

test:
	@python build.py
