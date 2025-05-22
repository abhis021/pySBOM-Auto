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
