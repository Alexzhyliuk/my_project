from setuptools import find_packages, setup 

setup( 
    name="cardsgames",
    version="0.0.1",
    description="A small cards games with tests for its",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pytest==5.1.0"],
    author="Alexandr Zhyliuk",
    author_email="alexzhyliuk3@gmail.com",
    url="https://github.com/Alexzhyliuk/my_project",
)