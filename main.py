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