# aunties

For working with ontologies

- Pull the latest GDB Master Ontology and check if any new fields are present:
```python
import aunties.helpers as ah
ah.gdb_download_telemetry()
ah.compare_telemetry_fields()
```

- If differences exist in the telemetry fields:
