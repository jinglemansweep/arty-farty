#!/bin/bash

while true; do
    echo "Launching ArtyFarty..."
    /opt/workspace/venv/bin/python3 -m artyfarty
    echo
    echo "Sleeping for ${SLEEP_DELAY}..."
    sleep ${SLEEP_DELAY}
    echo
done