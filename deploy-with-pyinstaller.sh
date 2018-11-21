rm -r "dist/"
LD_LIBRARY_PATH=~/.pyenv/versions/3.7.0/lib python -m PyInstaller --name tsukushi -p tsukushi/ -F  tsukushi/main.py
cp -v "tsukushi/tsukushi.kv" "dist/"
cp -v -r "tsukushi/images/" "dist/images/"
cp -v -r "tsukushi/fonts/" "dist/fonts/"
