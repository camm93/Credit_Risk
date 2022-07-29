# Credit_Risk

Create an app to estimate credit score and predict the outcome of future loans in terms of "Fully Paid or Charged Off".

This approach can be used to help both potential loan takers and financial institutions. The former will be able to estimate whether or not will be able to pay his/her financial obligations based on the loan conditions. Similarly, a financial institution can determined if a given loan can be granted.

Temporarily available at http://creditrisk.eastus.cloudapp.azure.com:8050/scorecard until the free Azure coupon expires XD

## Steps
- Data Collection from ![Kaggle - Lending Club](https://www.kaggle.com/datasets/ethon0426/lending-club-20072020q1)
- Data Cleaning
- Feature Selection
- Statistical Analysis
- EDA
- Modelling (Random Forest Regressor and Classifier)
- Dashboard and Presentation

## Tech Stack
<img height="40" width="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />&emsp;</img>
<img height="40" width="40" src="https://user-images.githubusercontent.com/88005878/181798815-09cc7597-a415-4409-9255-c1a6b95d7445.png" alt="jupyter notebook"/>&emsp;</img> <img height="32" width="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png">&emsp;</img> <img height="40" width="45" src="https://pandas.pydata.org/static/img/pandas.svg" >&emsp;</img> <img height="32" width="75" src="https://user-images.githubusercontent.com/88005878/181806232-17940c5a-67de-4eed-892a-82f5f2323912.PNG" alt="dash">&emsp;</img> <img height="40" width="60" src="https://user-images.githubusercontent.com/88005878/181806514-812cf580-3dfe-47ad-b1f8-8e2bf0e6ea2a.PNG" alt="sklearn">&emsp;</img>


## Cloning this repo:
On a terminal...
- Alternative 1
Via web URL:
```git clone https://github.com/DanielDi/Credit_Risk.git```
- Alternative 2
Via ssh key:
```git clone git@github.com:DanielDi/Credit_Risk.git```

## Requirements
- virtualenv
    - Install using "pip3 install virtualenv"
- docker

## Execute notebooks
1. Create virtual environment
```bash
virtualenv -p python3 env
```
2. Activate virtual environment
```bash
.\env\Scripts\activate
```
3. Install dependencies
```bash
pip install -r .\project\requirements.txt
```
3. Change the python interpreter

## Execute dash application
1. Open the directory project in terminal 
2. Build the project:
```bash
docker build -t docker-dash project/.
```
3. Run the project:
```
docker run --name dash-project -it --mount type=bind,source="$(pwd)"/project/app,target=/usr/src/app -p 8050:8050 docker-dash
```
4. Open in a browser http://localhost:8050

## Docker commands
```
- Check images:
docker images

- Check containers:
docker ps

-stop project
docker stop dash-project

-restart project
docker restart dash-project

- start project again
docker start dash-project

```
