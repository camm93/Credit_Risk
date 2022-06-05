# Credit_Risk

## Cloning this repo:
On a terminal...
- Alternative 1
Via web URL:
```git clone https://github.com/DanielDi/Credit_Risk.git```
- Alternative 2
Via ssh key:
```git clone git@github.com:DanielDi/Credit_Risk.git```

## Requirements
- docker

## Execute
1. Open a terminal
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
