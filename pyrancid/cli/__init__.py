from pyrancid.loaders import config_loader
import click
import os
import sys
from ruamel.yaml import YAML


@click.group()
def main():
    # setup the logger in main with a default logging config
    pass


def _get_config_default():
    # XDG standard for configs in home directory
    home_config = f"{os.environ.get('HOME')}/.config/pyrancid/prancid.conf"
    # Global etc location
    global_config = '/etc/pyrancid/pyrancid.conf'

    return home_config, global_config


@click.command()
@click.option('--config', multiple=True, default=_get_config_default)
@click.option('-v', '--verbose', count=True)
def checkconfig(config, verbose):
    loadable_configs = []
    for c in config:
        if not os.path.exists(c):
            print(c, "doesnt exist")
        loadable_configs.append(c)

    # return config
    config = config_loader(loadable_configs)
    if isinstance(config, dict):
        if verbose >= 2:
            print(YAML().dump(config, sys.stdout))
        print('Config is good')


main.add_command(checkconfig)

if __name__ == "__main__":
    main()
