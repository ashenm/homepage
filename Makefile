default:
	$(MAKE) build
	$(MAKE) serve

install:
	./.travis/install.py

serve:
	./.travis/serve.py

build: _data/routes.yml
	./.travis/build.py

clean:
	./.travis/clean.py
