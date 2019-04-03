#!/bin/bash

tmux &
tmux new-window -n:TG-Encrypt &
tmux split-window &
tmux select-pane -t :.+
python updates.py  $1 &
tmux select-pane -t :.+
python send.py $1
