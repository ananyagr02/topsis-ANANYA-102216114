from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="topsis-ANANYA-102216114", 
    version="1.0.3",  
    author="Ananya Gaur", 
    author_email="hiananya02@gmail.com",  
    description="A Python package for performing TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) to rank the entries in a dataset.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ananyagr02/topsis-ANANYA-102216114",  
    packages=find_packages(), 
    py_modules=["topsis"],  
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0"
        
    ],
    entry_points={
        "console_scripts": [
            "topsis-ANANYA-102216114=topsis_102216114:main",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.7",  
)
