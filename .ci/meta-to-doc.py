#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import os
import yaml

meta_file_path = "./meta/main.yml"
argspecs_file_path = "./meta/argument_specs.yml"
template_file_path = "./.ci"
template_file_name = "README.md.j2"
output_file_path = "README.md"

def parse_yaml_file(yaml_file):
    if not os.path.isfile(yaml_file):
        raise FileNotFoundError(f"YAML file {yaml_file} does not exist.")

    with open(yaml_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    return data


def generate_argspecs_variables(specs):
    """Generates the Markdown documentation based on the argument specifications.

    Args:
        specs (dict): The argument specifications.

    Returns:
        str: The complete Markdown documentation.
    """
    section_variables = ""
    for k, v in specs.items():
        section_variables += f"### {k}\n"
        section_variables += "\n"
        section_variables += "| Variable | Type | Required | Choices | Default | Description |\n"
        section_variables += "| --- | --- | --- | --- | --- | --- |\n"
        for kv, vv in v.items():
            if 'options' in kv:
                for o, ov in vv.items():
                    md_line = f"| `{o}` "
                    for ok in ['type','required','choices','default','description']:
                        if ok in ov:
                            if ok == 'description':
                                description = ' <br />'.join(ov[ok])
                                md_line += f"| {description} "
                            else:
                                md_line += f"| `{ov[ok]}` "
                        else:
                            md_line += f"| "
                    section_variables += f"{md_line}|\n"
                    if 'options' in ov:
                        for oo, oov in ov['options'].items():
                            md_line = f"| `{o}.{oo}` "
                            for ok in ['type','required','choices','default','description']:
                                if ok in oov:
                                    if ok == 'description':
                                        description = ' <br />'.join(oov[ok])
                                        md_line += f"| {description} "
                                    else:
                                        md_line += f"| `{oov[ok]}` "
                                else:
                                    md_line += f"| "
                            section_variables += f"{md_line}|\n"
        section_variables += "\n"
    return section_variables

def get_template(template_path):
    try:
        env = Environment(loader=FileSystemLoader(template_file_path))
        return env.get_template(template_path)
    except Exception as e:
        print(f"Error loading template: {e}")
        return None

def render_template(template, context, output_file):
    try:
        rendered_output = template.render(context)
        with open(output_file, "w", encoding="UTF-8") as file:
            file.write(rendered_output)
        print(f"Successfully rendered and wrote {output_file}")
    except Exception as e:
        print(f"Error rendering template or writing file: {e}")


if __name__ == "__main__":
    arg_specs = generate_argspecs_variables(parse_yaml_file(argspecs_file_path)['argument_specs'])
    meta = parse_yaml_file(meta_file_path)
    template = get_template(template_file_name)
    context = {
        'arg_specs': arg_specs,
        'meta': meta
    }
    render_template(template, context, output_file_path)
