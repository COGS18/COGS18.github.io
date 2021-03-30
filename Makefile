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
	rm -rf materials_bardolph
	rm -rf labs
	rm -rf projects

serve:
	#bundle exec guard
	bundle exec jekyll serve

textbook:
	python scripts/clean.py
	
	# Copy & build materials - Ellis
	git clone --depth 1 https://github.com/COGS18/LectureNotes-Sp21-Ellis materials

	# Copy & build materials - Bardolph
	git clone --depth 1 https://github.com/COGS18/LectureNotes-Sp21-Bardolph materials_bardolph
	#rm materials_bardolph/README.md

	# Copy & build coding labs
	# git clone --depth 1 https://github.com/COGS18/CodingLabs labs
	# rm -rf labs/README.md
	# rm -rf Archive
	# mv labs/source/* labs	
	# rm -rf labs/source

	# Copy & build project info
	# git clone --depth 1 https://github.com/COGS18/projects projects
	# rm projects/README.md

	jupyter-book build ./
	# get project template 
	# cp projects/ProjectTemplate.zip _build/html/assets/intro/projects/
	
	# copy first day of slides to _build
	cp assets/intro/01_welcome.pdf _build/html/assets/intro/
	
	# copy non-md images to build
	mkdir _build/html/_images
	cp materials/img/* _build/html/_images/


	rm -rf labs

	rm -rf materials
	rm -rf materials_bardolph

	rm -rf projects


home:
	rm _build/intro.md
	rm -rf _build/intro
	cp -r landing content
	python scripts/generate_book.py

publish:
	ghp-import -n -p -f ./_build/html
