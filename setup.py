from setuptools import setup, find_packages

setup(
    name="drinkadvisorbot",
    version="1.0.0",
    description="Telegram-бот, помощник по напиткам",
    author="Egor",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==20.3",
        "python-dotenv==1.0.1",
    ],
    python_requires=">=3.8",
)
