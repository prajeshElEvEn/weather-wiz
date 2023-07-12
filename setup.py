from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Get weather information from the command line'
LONG_DESCRIPTION = 'A package that allows you to get weather information from the command line using the OpenWeatherMap API.'

# Setting up
setup(
    name="weather_wiz",
    version=VERSION,
    author="Pranjal Agarawal",
    author_email="prajesh.eleven118@gamil.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['certifi==2023.5.7', 'charset-normalizer==3.1.0', 'idna==3.4', 'pyfiglet==0.8.post1',
                      'python-dotenv==1.0.0', 'requests==2.31.0', 'tabulate==0.9.0', 'termcolor==2.3.0', 'urllib3==2.0.2'],
    keywords=['python', 'weather', 'weather information', 'weather-wiz', 'weather-wiz package', 'weather-wiz python', 'OpenWeatherMap', 'OpenWeatherMap API', 'CLI', 'command line',
              'command line interface', 'command line tool', 'tool', 'command line weather tool', 'command line weather information tool', 'command line weather information', 'command line weather'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
