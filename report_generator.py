# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 Your Name <your.email@example.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from weasyprint import HTML

def generate_report(cve_data: dict, output_dir='reports', as_pdf=False):
    os.makedirs(output_dir, exist_ok=True)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    html_content = template.render(
        timestamp=timestamp,
        cve_data=cve_data
    )

    if as_pdf:
        output_path = os.path.join(output_dir, f"report_{timestamp}.pdf")
        HTML(string=html_content).write_pdf(output_path)
    else:
        output_path = os.path.join(output_dir, f"report_{timestamp}.html")
        with open(output_path, 'w') as f:
            f.write(html_content)

    return output_path
