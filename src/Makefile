run : main.py mainwindow.ui
	python3 main.py

install :
	pip install -r requirements.txt

build : main.py mainwindow.ui
	pyuic5 mainwindow.ui -o file.py
	sed 's/from mygl import/from graphic.mygl import/g' file.py > ./graphic/ui_mainwindow.py
	rm file.py
