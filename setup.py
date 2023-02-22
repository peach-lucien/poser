from setuptools import setup, find_packages

setup(
    name="poser",
    version="1.0.1",
    description="Poser analysis package",
    author="Robert Peach",
    author_email="peach_r@ukw.de",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.2",
        "scipy>=1.4.1",
        "tqdm>=4.45.0",
        "scikit-learn>=0.23.1",
        "matplotlib>=1.4.3",
        "seaborn>=0.9.0",
        "shap>=0.35.0",
        "pandas>=1.0.3",
        "wget>=3.2",
        "sympy>=1.4",
        "joblib>=0.14.1",
        "IPython>=7.19.0",
        "xgboost>=1.3.3",
        "simdkalman>1.0.0",
        "neurodsp>=2.1.0"
    ],
    entry_points={"console_scripts": ["poser=poser.app:cli"]},
)
