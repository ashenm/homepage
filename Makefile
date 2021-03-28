.DEFAULT_GOAL = help
BUNDLE_PATH ?= vendor/bundle

.PHONY: build
build: _data/routes.yml clean ## build site
	BUNDLE_PATH=$(BUNDLE_PATH) ./_scripts/build.py

.PHONY: clean
clean: ## clean build artifacts
	BUNDLE_PATH=$(BUNDLE_PATH) ./_scripts/clean.py

.PHONY: culminate
culminate: ## trigger reverse-dependency builds
	BUNDLE_PATH=$(BUNDLE_PATH) ./_scripts/culminate.py

.PHONY: help
.SILENT: help
help: ## show make targets
	BUNDLE_PATH=$(BUNDLE_PATH) awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: help
install: ## install requisite packages
	BUNDLE_PATH=$(BUNDLE_PATH) ./_scripts/install.py

.PHONY: serve
serve: build ## locally serve site
	BUNDLE_PATH=$(BUNDLE_PATH) ./_scripts/serve.py
