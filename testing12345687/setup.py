from setuptools import find_packages, setup

setup(
    name="testing12345687",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "testing12345687": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core>=1.4.0",
        "dbt-duckdb",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

