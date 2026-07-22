curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.15.0b2
cd /tmp
pip3 install pillow
pip3 install opencv-python
pip3 install pathlib
curl https://github.com/nepusoft/sony_playingback_to_gif/raw/refs/heads/main/install.py > install.py
python3 install.py
rm install.py
