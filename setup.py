from setuptools import find_packages,setup
setup(
    name="MCQ generator",
    version="0.0.1",
    author="krishna",
    author_email="krishnavardhan2906@gmail.com",
    install_requries=["openai","langchain","streamlit","python-dotenv","PyPDF2"],

    packages=find_packages()
)