.PHONY: help textbook clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  textbook    to convert the `notebooks/` folder into Jekyll markdown in `chapters/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

textbook:
	python scripts/clean.py

	rm -rf notebooks
	git clone --depth 1 https://github.com/COGS18/materials notebooks
	rm notebooks/README.md

	python scripts/generate_summary_from_folders.py --overwrite
	python scripts/generate_textbook.py

	python scripts/copy_for_download.py

	rm -rf notebooks

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py

serve:
	bundle exec jekyll serve
