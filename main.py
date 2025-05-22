# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 Your Name <your.email@example.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from sbom_parser import parse_sbom
from cve_checker import check_cves
from report_generator import generate_report

def main():
    sbom_path = 'sample_sbom.spdx.json'  # or sample_sbom.json
    packages = parse_sbom(sbom_path, format='spdx')  # or 'cyclonedx'
    cve_results = check_cves(packages)
    report_path = generate_report(cve_results, as_pdf=True)
    print(f"Compliance report saved at: {report_path}")


if __name__ == "__main__":
    main()