#! /bin/sh



export PYTHONPATH=../../src:$PYTHONPATH

python3 -m programy.clients.restful.flask.webchat.client --config ../../config/xnix/config.webchat.yaml --cformat yaml --logging ../../config/xnix/logging.yaml --bot_root ../../config/xnix
