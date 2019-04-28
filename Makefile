


.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  notebook    to convert the `content/` folder into Jekyll markdown in `_build/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

book:
	python scripts/generate_book.py

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py
	rm -rf content

serve:
	#bundle exec guard
	bundle exec jekyll serve

textbook:
	python scripts/clean.py

	# Copy & build landing pages
	cp -r landing content

	# Copy & build materials
	git clone --depth 1 https://github.com/COGS18/materials content/materials
	rm content/materials/README.md

	# Copy & build assignments
	git clone --depth 1 https://github.com/COGS18/assignments content/assignments
	rm content/assignments/README.md

	# Copy & build coding labs
	git clone --depth 1 https://github.com/COGS18/codinglabs content/labs
	rm content/labs/README.md

	# Copy & build project info
	git clone --depth 1 https://github.com/COGS18/projects content/projects
	rm content/projects/README.md

	python scripts/generate_book.py

	rm -rf content

home:
	rm _build/intro.md
	rm -rf _build/intro
	cp -r landing content
	python scripts/generate_book.py
