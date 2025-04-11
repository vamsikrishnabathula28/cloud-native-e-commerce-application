@echo off
cd %~dp0
start http://localhost:8000/index.html
python server.py 