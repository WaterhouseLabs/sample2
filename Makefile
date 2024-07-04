install:
	cd src && pipenv install
#> make dev-install

lint:
	find . -iname "*.py" | xargs pylint
#> make lint

lintme:
	autopep8 --in-place --aggressive --aggressive $(f)
#> make lintme f=src/app/main.py

lintall:
	find . -iname "*.py" | xargs autopep8 --in-place --aggressive --aggressive $(f)
#> make lintme f=src/app/main.py

testme:
	ptw -c src/
#> make test

launch:
	docker build -t streamlit-app:latest src &&  docker run -p 8080:8080 streamlit-app
#>make launch

local-launch:
	cd src && streamlit run main.py --server.port=8080", "--server.address=0.0.0.0 --log-level debug && cd ..
#>make local-launch:
