import os
import subprocess

{% if cookiecutter.git_init -%}
try:
    subprocess.run(['git', 'init'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: Failed to initialize git repository. {e}")
    exit(1)
{%- endif %}

os.rename('.gitignore.tmp', '.gitignore')
