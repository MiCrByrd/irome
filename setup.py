from setuptools import setup

setup(
   name="irome",
   version="0.1",
   description="Model implementations for IROME.",
   author="Michael Byrd",
   author_email="mcbyrd100@gmail.com",
   packages=["irome"], 
   python_requires=">=3.8.0",
   install_requires=[
       "numpy",
       "pandas"
    ]
)