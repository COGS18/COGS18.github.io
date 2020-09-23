.PHONY: help book clean serve textbook

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  notebook    to convert the `content/` folder into Jekyll markdown in `_build/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

book:
	jupyter-book build ./

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py
	rm -rf materials
	rm -rf labs
	rm -rf projects

serve:
	#bundle exec guard
	bundle exec jekyll serve

textbook:
	python scripts/clean.py

	# Copy & build materials
	git clone --depth 1 https://github.com/COGS18/LectureNotes-Fa20 materials
	rm materials/README.md


	# Copy & build coding labs
	# git clone --depth 1 https://github.com/COGS18/CodingLabs/answers labs


	# Copy & build project info
	# git clone --depth 1 https://github.com/COGS18/projects projects
	# rm projects/README.md

	jupyter-book build ./

	rm -rf labs
	rm -rf materials
	rm -rf projects


home:
	rm _build/intro.md
	rm -rf _build/intro
	cp -r landing content
	python scripts/generate_book.py
