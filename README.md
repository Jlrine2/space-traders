# Space Traders SDK

## Installation
This project is not hosted in PyPi so must be installed using the git source
```
pip install git+https://github.com/Jlrine2/space-traders.git
```

## Usage
### Create a client

```python
from st_api import Client

# Register new agent
client = Client.new("COSMOS", "MY_UNIQUE_SYMBOL")

# Or use an existing one
client = Client("token")
```

### Make API requests
```python
# Get agent Details
client.agents.get_agent()

# Get Ships
client.fleet.list_ships()
```

### SDK organization

This SDK is organized to be easy to use when following the [API reference](https://spacetraders.stoplight.io/docs/spacetraders/)

Each category in the docs (Agents, Contracts, Factions, Fleet, Systems) has an attribute under client, and each of those
attributes have functions for the different endpoints. For example, the endpoint `Scan Ships` is located at `Fleet > Scan Ships`
so the SDK method for it is `client.fleet.scan_ships()`


## Updating models
This project includes the `api-docs` for Space Traders as a git submodule, you can use that to bring the docs into this 
project with `git submodule init` followed by `git submodule update --remote`.

Once the files for the API docs are clones locally you can run `python model_gen.py` to update the datamodels.