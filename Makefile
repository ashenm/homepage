default:
	$(MAKE) build
	$(MAKE) serve

environment:
	./.travis/environment.py

install:
	./.travis/install.py

serve:
	./.travis/serve.py

build: _data/routes.yml
	./.travis/build.py

culminate:
	./.travis/culminate.py

clean:
	./.travis/clean.py
