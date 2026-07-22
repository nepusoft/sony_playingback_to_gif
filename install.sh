cd /tmp
pip3 install pillow
pip3 install opencv-python
pip3 install pathlib
curl https://github.com/nepusoft/sony_playingback_to_gif/raw/refs/heads/main/install.py > install.py
chmod +x install.py
python3 install.py
rm install.py
