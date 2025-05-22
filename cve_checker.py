import requests
import time

def check_cves(package_list: list) -> dict:
    results = {}
    for package in package_list:
        name, version = package.split('@')
        try:
            url = f"https://ossindex.sonatype.org/api/v3/component-report"
            response = requests.post(url, json={"coordinates": [f"pkg:pypi/{name}@{version}"]})
            data = response.json()
            results[package] = data[0].get('vulnerabilities', [])
            time.sleep(1)  # avoid rate limiting
        except Exception as e:
            results[package] = [{"error": str(e)}]
    return results