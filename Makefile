.DEFAULT_GOAL = help

.PHONY: build
build: _data/routes.yml clean ## build site
	./.travis/build.py

.PHONY: clean
clean: ## clean build artifacts
	./.travis/clean.py

.PHONY: culminate
culminate: ## trigger reverse-dependency builds
	./.travis/culminate.py

.PHONY: environment
environment:
	./.travis/environment.py

.PHONY: help
.SILENT: help
help: ## show make targets
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: help
install: ## install requisite packages
	./.travis/install.py

.PHONY: serve
serve: build ## locally serve site
	./.travis/serve.py
