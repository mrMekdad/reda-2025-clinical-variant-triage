from setuptools import setup

setup(
    name="reda-2025-clinical-variant-triage",
    version="0.1.0",
    description="Variant triage helpers with review queues, labels, and concise evidence bundles.",
    author="Red@",
    packages=["clinical_variant_triage"],
    package_dir={"": "src"},
)
