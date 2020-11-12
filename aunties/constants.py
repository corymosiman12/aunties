import os

GDB_TELEM_FILE_NAME = 'telemetry_fields.yaml'
GDB_NEW_FILE_NAME = 'telemetry_fields_new.yaml'
GDB_TELEM_REMOTE = f"https://raw.githubusercontent.com/google/digitalbuildings/master/ontology/yaml/resources/fields/{GDB_TELEM_FILE_NAME}"
FILES_DIR = os.path.join(os.path.dirname(__file__), 'files')
