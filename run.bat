@echo OFF

cd a-star-vs-dls\src
python write_graph.py
python main.py
cd ..\..
cd graphs-for-avd\src
python gen_graph.py
python color_graph.py
python make_png.py
cd ..\..