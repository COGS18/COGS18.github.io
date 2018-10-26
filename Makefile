.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  book    to convert the `notebooks/` folder into Jekyll markdown in `chapters/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

book:
	python scripts/generate_book.py

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py

serve:
	#bundle exec guard
	bundle exec jekyll serve

textbook:
	python scripts/clean.py

	# Copy & build materials
	rm -rf content/materials
	git clone --depth 1 https://github.com/COGS18/materials content/materials
	rm content/materials/README.md

	# Copy & build assignments
	rm -rf content/assignments
	git clone --depth 1 https://github.com/COGS18/assignments content/assignments
	rm content/assignments/README.md

	# Copy & build coding labs
	rm -rf content/labs
	git clone --depth 1 https://github.com/COGS18/codinglabs content/labs
	rm content/labs/README.md

	python scripts/generate_book.py
