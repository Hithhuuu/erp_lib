from setuptools import setup, find_packages

setup(

    name='erp_quartering_lib',  # Updated name
    version='0.1.2',

    packages=find_packages(),
    install_requires=[
        'fastapi==0.112.1',
        'SQLAlchemy==2.0.32',
        'psycopg2-binary==2.9.9',
        'pydantic-settings==2.4.0'
    ],
    url='https://repo.epps-erp.in/navyojana/api/lib/erp-quartering-lib.git',  # Update URL if necessary
    author='Abhinesh Kumar',
    author_email='abhineshkumar@epps-erp.com',
    description='A Python library for ERP systems using PostgreSQL and SQLAlchemy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='EPPS'
)
