import setuptools 

with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

Repo_name="kidney_disease_prediction"
Author_user_name="nagamalliparasa"
Src_repo="cnnClassifier"
Author_email="nagamallirgukt@gmail.com"

setuptools.setup(
    name=Src_repo,
    version=__version__,
    author=Author_user_name,
    author_email=Author_email,
    description="A small python package for cnn app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_user_name}/{Repo_name}",
    project_urls={
        "Bug Tracker":f"https://github.com/{Author_user_name}/{Repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)