help:  ## This help 
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Clean python bytecodes, optimized files, logs, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@echo 'Temporary files deleted'

docker-compose-up: clean  ## Raise docker-compose for development environment
	@docker-compose up -d

docker-compose-stop: clean  ## Stop docker-compose for development environment
	@docker-compose stop

docker-compose-rm: docker-compose-stop ## Delete the development environment containers
	@docker-compose rm -f

requirements-pip:  ## Install the APP requirements
	@pip install --upgrade pip
	@pip install -r requirements/base.txt
	@pip install -r requirements/development.txt

format:  ## Run black auto formatting code style in the project
	@black app.py

lint: clean  ## Run pylint linter
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc  app.py --errors-only
	@printf '\n FINISHED! \n --- \n'