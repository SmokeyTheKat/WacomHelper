install:
	sudo echo "" > /usr/bin/wacomhelper
	sudo echo "#!/bin/bash" >> /usr/bin/wacomhelper
	sudo echo "python3 /usr/share/wacomhelper/wacomhelper.py \"\$$@\"" >> /usr/bin/wacomhelper
	sudo mkdir /usr/share/wacomhelper -p
	sudo cp ./wacomhelper.py /usr/share/wacomhelper/
	sudo chmod +x /usr/bin/wacomhelper
