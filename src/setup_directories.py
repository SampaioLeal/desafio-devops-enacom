import os

LOCAL_INPUT_DIR = "inputs"
LOCAL_OUTPUT_DIR = "outputs"

TMP_INPUT_DIR = "/tmp/inputs"
TMP_OUTPUT_DIR = "/tmp/outputs"


def setup_directories():
    os.makedirs(LOCAL_INPUT_DIR, exist_ok=True)
    os.makedirs(LOCAL_OUTPUT_DIR, exist_ok=True)

    os.makedirs(TMP_INPUT_DIR, exist_ok=True)
    os.makedirs(TMP_OUTPUT_DIR, exist_ok=True)
