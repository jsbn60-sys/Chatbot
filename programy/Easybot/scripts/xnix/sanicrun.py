#! /bin/sh
clear
python3 -m programy.clients.restful.sanic.client --config ./config.yaml --cformat yaml --logging ./logging.yaml
