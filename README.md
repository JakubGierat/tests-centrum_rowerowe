To run tests:

1. You have to get poetry. Install instruction link below. If you have poetry already go to step 2. 
```
https://python-poetry.org/docs/#installation
```
2. Initialize new poetry shell. It will create new virtual environment.
```
$ poetry shell
```
3. Install all required dependecies from .toml file.
```
$ poetry install
```
Notice: the poetry.lock file prevents you from automatically getting the latest versions of your dependencies. To update to the latest versions, use the update command. This will fetch the latest matching versions (according to your pyproject.toml file) and update the lock file with the new versions.
```
$ poetry update
```
4. Run tests
```
$ pytest tests
```

