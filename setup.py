# Base imports
from setuptools import setup

# Project imports
from jcalc.settings import JCALC_VERSION

setup(
    name="jcalc",
    version=JCALC_VERSION,
    description="jcalc: Calculate NMR J values from \
        Molecular Dynamics simulations",
    url="https://github.com/Joaodemeirelles/jcalc/",
    author="Joao Luiz de Meirelles",
    author_email="jldemeirelles@gmail.com",
    licence="Academic",
    packages=[
        "jcalc",
        "jcalc.tools",
        "db_generator.db_stats",
        "db_generator.db_writer",
        "db_generator.logger",
    ],
    scripts=["jcalc/jcalc"],
    zip_safe=False
)
