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

	# Copy & build materials - Ellis
	git clone --depth 1 https://www.github.com/COGS18/LectureNotes-COGS18.git materials

	# Copy & build coding labs
	# git clone --depth 1 https://github.com/COGS18/CodingLabs.git labs
	# rm -rf labs/README.md
	# rm -rf labs/Archive
	# rm labs/CL1-Tooling.ipynb
	# new method is to have separate directory for the answers distributed on Website
	# manually add them to the directory as you want to distribute, remove at
	# beginning of the quarter
	# mv labs/answers-for-website/* labs
	rm -rf labs/source

	# Copy & build project info
	git clone --depth 1 https://www.github.com/COGS18/Projects.git projects
	rm projects/README.md

	jupyter-book build ./
	# get project template
	mkdir -p _build/html/assets/intro/projects/
	cp assets/intro/projects/ProjectTemplate.zip _build/html/assets/intro/projects/

	# copy first day of slides to _build
	cp assets/intro/01_welcome.pdf _build/html/assets/intro/

	mkdir -p _build/html/assets/intro/exams/
	cp assets/intro/exams/E1_Sp23_Answers.pdf _build/html/assets/intro/exams
	cp assets/intro/exams/E2_Sp23_Answers.pdf _build/html/assets/intro/exams

	# copy non-md images to build
	 mkdir -p _build/html/_images
	 cp materials/img/* _build/html/_images/


	# rm -rf labs
	rm -rf materials
	rm -rf projects


home:
	rm _build/intro.md
	rm -rf _build/intro
	cp -r landing content
	python scripts/generate_book.py

publish:
	ghp-import -n -p -f ./_build/html
