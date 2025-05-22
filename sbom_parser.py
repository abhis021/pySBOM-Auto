from spdx.parsers.jsonparser import Parser as SPDXParser
from spdx.parsers.loggers import StandardLogger
from spdx.document import Document
import json

def parse_spdx(file_path: str) -> list:
    logger = StandardLogger()
    with open(file_path, 'r') as f:
        document = SPDXParser(logger).parse(f)
    return [f"{p.name}@{p.version}" for p in document.packages]

def parse_sbom(file_path: str, format='cyclonedx') -> list:
    if format == 'cyclonedx':
        from cyclonedx.parser.json import JSONParser
        with open(file_path, 'r') as f:
            data = json.load(f)
        bom = JSONParser(json_data=data).bom
        return [f"{c.name}@{c.version}" for c in bom.components]
    elif format == 'spdx':
        return parse_spdx(file_path)
    else:
        raise ValueError("Unsupported SBOM format")
