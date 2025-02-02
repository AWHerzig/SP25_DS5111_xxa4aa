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
