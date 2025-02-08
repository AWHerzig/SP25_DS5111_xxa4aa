# SP25_DS5111_xxa4aa
Aidan Herzig Repository for Software and Automation Skills


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

This file lays out which packages are needed. Right now, it is only `pandas` and `lxml` 

## 3. Starting virtual enviornment

```bash
make update
```

Starts the enviornment and updates the packages in requirements.txt

## 4. Run a job in makefile to test browser

```bash
make ygainers.csv
```

## 5. Repository Tree
```
.
├── README.md
├── google-chrome-stable_current_amd64.deb
├── init.sh
├── makefile
├── requirements.txt
├── sample_data
│   ├── ygainers.csv
│   └── ygainers.html
└── scripts
    └── install_chrome_headless.sh
```

An example of `ygainers.csv` is available in `sample_data/` directory.










