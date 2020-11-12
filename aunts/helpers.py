import os
from typing import Tuple

import yaml
import requests

import aunts.constants as ac


def gdb_download_telemetry() -> None:
    r = requests.get(ac.GDB_TELEM_REMOTE)
    if r.status_code == 200:
        save_path = os.path.join(ac.FILES_DIR, ac.GDB_NEW_FILE_NAME)
        with open(save_path, 'wb+') as fp:
            fp.write(r.content)


def compare_telemetry_fields() -> Tuple[set, set]:
    f_new = os.path.join(ac.FILES_DIR, ac.GDB_NEW_FILE_NAME)
    f_old = os.path.join(ac.FILES_DIR, ac.GDB_TELEM_FILE_NAME)

    new_fields = create_set_of_fields(f_new)
    old_fields = create_set_of_fields(f_old)

    new_fields_present = new_fields.difference(old_fields)
    old_fields_removed = old_fields.difference(new_fields)
    diff = new_fields_present.union(old_fields_removed)
    if len(new_fields_present) > 0 or len(old_fields_removed) > 0:
        print("Differences exist in the following fields")

    return diff


def create_set_of_fields(file_path):
    with open(file_path, 'r') as fp:
        data = yaml.safe_load_all(fp)
        data = list(data)
    combined = []
    for item in data:
        combined += item['literals']

    fields = set()
    for item in combined:
        fields.add(freeze_fields(item))
    return fields


def freeze_fields(d):
    if isinstance(d, dict):
        return frozenset((key, freeze_fields(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze_fields(value) for value in d)
    return d
