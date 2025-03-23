# SP25_DS5111_xxa4aa
Aidan Herzig Repository for Software and Automation Skills

[![Feature Validation](https://github.com/AWHerzig/SP25_DS5111_xxa4aa/actions/workflows/validations.yml/badge.svg?branch=LAB-03_csv_normalizer)](https://github.com/AWHerzig/SP25_DS5111_xxa4aa/actions/workflows/validations.yml)


# Instructions to setup the VM

## 1. Update packages

```bash
sudo apt update
```

## 2. Set up git credentials (if not done already)

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

## 3. Generate SSH Key (if not done already)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Be sure to add the public key to GitHub.

## 4. Clone this repository

```bash
git clone git@github.com:AWHerzig/SP25_DS5111_xxa4aa.git
```

## 5. Run the init script

Navigate to where the repository has been cloned

```bash
./init.sh
```

# Project specific setup

## 1. Install Chrome Headless Browser

```bash
./scripts/install_chrome_headless.sh
```

This will also test the installation with example.com

## 2. requirements.txt

This file lays out which packages are needed and the versions that ought to be used.

## 3. Starting virtual enviornment

```bash
make update
```

Starts the enviornment and updates the packages in requirements.txt

## 4. Run a job in makefile to test browser

```bash
make ygainers.csv
```

Using the `gainers` job, user can get an output csv file with a timestamp. The SRC variable will dictate which source is used.

```bash
make gainers SRC=yahoo
```

OR

```bash
make gainers SRC=wsj
```

Data is published to the `sample_data/` subdirectory.

## 5. Repository Tree

This is a current snapshot of the repository tree (18 Mar 2025)

```
.
├── README.md
├── __pycache__
│   └── get_gainer.cpython-312.pyc
├── bin
│   ├── __pycache__
│   │   └── normalize_csv.cpython-312.pyc
│   ├── gainers
│   │   ├── __pycache__
│   │   │   ├── base.cpython-312.pyc
│   │   │   ├── factory.cpython-312.pyc
│   │   │   ├── wsj.cpython-312.pyc
│   │   │   └── yahoo.cpython-312.pyc
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── wsj.py
│   │   └── yahoo.py
│   └── normalize_csv.py
├── get_gainer.py
├── google-chrome-stable_current_amd64.deb
├── init.sh
├── makefile
├── pylintrc
├── requirements.txt
├── sample_data
│   ├── archive
│   │   ├── wjsgainers.csv
│   │   ├── wjsgainers.html
│   │   ├── wjsgainers_norm.csv
│   │   ├── ygainers.csv
│   │   ├── ygainers.html
│   │   └── ygainers_norm.csv
│   ├── wjsgainers_2025-03-07_15-11-11.csv
│   ├── wjsgainers_2025-03-07_15-55-35.csv
│   ├── wjsgainers_2025-03-10_12-43-37.csv
│   ├── wjsgainers_2025-03-10_16-06-58.csv
│   ├── wjsgainers_2025-03-14_17-49-46.csv
│   ├── wjsgainers_2025-03-14_17-53-26.csv
│   ├── wjsgainers_2025-03-17_09-31-39.csv
│   ├── wjsgainers_2025-03-17_12-30-33.csv
│   ├── wjsgainers_2025-03-17_16-01-24.csv
│   ├── wjsgainers_2025-03-18_09-31-38.csv
│   ├── wjsgainers_2025-03-18_12-30-34.csv
│   ├── wjsgainers_2025-03-18_16-01-33.csv
│   ├── ygainers_2025-03-07_15-10-51.csv
│   ├── ygainers_2025-03-07_15-50-13.csv
│   ├── ygainers_2025-03-07_16-01-44.csv
│   ├── ygainers_2025-03-10_11-05-11.csv
│   ├── ygainers_2025-03-10_12-30-47.csv
│   ├── ygainers_2025-03-10_12-43-15.csv
│   ├── ygainers_2025-03-10_16-01-24.csv
│   ├── ygainers_2025-03-11_09-31-21.csv
│   ├── ygainers_2025-03-11_12-30-11.csv
│   ├── ygainers_2025-03-11_16-01-11.csv
│   ├── ygainers_2025-03-12_09-31-11.csv
│   ├── ygainers_2025-03-12_12-30-11.csv
│   ├── ygainers_2025-03-12_16-01-12.csv
│   ├── ygainers_2025-03-13_09-31-11.csv
│   ├── ygainers_2025-03-13_12-30-11.csv
│   ├── ygainers_2025-03-13_16-01-11.csv
│   ├── ygainers_2025-03-14_09-31-11.csv
│   ├── ygainers_2025-03-14_12-30-12.csv
│   ├── ygainers_2025-03-14_16-01-12.csv
│   ├── ygainers_2025-03-17_09-31-30.csv
│   ├── ygainers_2025-03-17_12-30-23.csv
│   ├── ygainers_2025-03-18_09-31-28.csv
│   ├── ygainers_2025-03-18_12-30-26.csv
│   └── ygainers_2025-03-18_16-01-23.csv
├── scripts
│   └── install_chrome_headless.sh
└── tests
    ├── __pycache__
    │   ├── test_adder.cpython-312-pytest-8.3.4.pyc
    │   ├── test_factory_architecture.cpython-312-pytest-8.3.4.pyc
    │   ├── test_generic.cpython-312-pytest-8.3.4.pyc
    │   └── test_normalize_csv.cpython-312-pytest-8.3.4.pyc
    ├── test_factory_architecture.py
    ├── test_generic.py
    └── test_normalize_csv.py

11 directories, 68 files
```










