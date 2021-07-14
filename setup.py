import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fetch_title",
    version="0.1.0",
    author="y_mrt",
    author_email="y.mrt@tuta.io",
    description="fetch a content from title tag in HTML file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cm-hirano-shigetoshi/python_sample_command",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['fetch_title = fetch_title.fetch_title:main']
    },
    python_requires='>=3.7',
)