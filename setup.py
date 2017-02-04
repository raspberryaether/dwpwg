from setuptools import setup, find_packages

setup(
    name = "dwpwg",
    use_scm_version = True,
    author = "Raspberry Aether",
    author_email = "raspberryaether@riseup.net",
    description = "(d)ice(w)are (p)ass(w)ord (g)enerator",
    keywords = ("diceware password passwords passphrase passphrases " +
                "security bitcoins monero crypto cryptocurrency " +
                "key keys keyphrase keyphrases encryption nsa " +
                "surveillance privacy private secret secrecy " +
                "generate generator dice d20 brainwallet wallet").split(),
    url = "https://github.com/raspberryaether/dwpwg",
    packages = find_packages(),
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'dwpwg = dwpwg.pwgen:main'
        ]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities"
    ],
    install_requires = [
        "pyparsing"
    ],
    setup_requires = [
        "setuptools_scm"
    ]
)
