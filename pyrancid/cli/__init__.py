from pyrancid.loaders import config_loader
import click
from click.termui import Choice
import os
import sys
import ruamel.yaml
import logging
from typing import Dict
from typing import Any


def _get_config_default():
    # XDG standard for configs in home directory
    home_config = f"{os.environ.get('HOME')}/.config/pyrancid/pyrancid.yaml"
    # Global etc location
    global_config = '/etc/pyrancid/pyrancid.yaml'

    return global_config, home_config


def _query_group_data(name: str):
    connection_type_choices = Choice(('SSH', 'Telnet'))
    group_data: Dict[str, Any] = {}
    group_name: str = click.prompt("Group name", type=str, default=name)
    auth_user: str = click.prompt("Group auth user", type=str)
    auth_pass: str = click.prompt(
        "Group auth password", hide_input=True, type=str)
    connection_type: str = click.prompt(
        "Group connection type",
        type=connection_type_choices,
        show_choices=True
    )

    group_data.update({
        'group_name': group_name.lower(),
        'group_auth_user': auth_user,
        'group_auth_pass': auth_pass,
        'connection_type': connection_type,
    })

    return group_data


CONFIG: Dict[str, Any] = {}


@click.group('main')
@click.option('-c', '--configs', multiple=True, default=_get_config_default)
def main(configs):
    yml = ruamel.yaml.YAML()
    # setup the logger in main with a default logging config
    if not configs:
        configs = _get_config_default()

    config_dict: Dict = {}
    for config in configs:
        try:
            with open(config, 'rt') as fp:
                config_dict.update(yml.load(fp.read()))
        except FileNotFoundError as e:
            print(e)

    CONFIG.update(config_dict)


@main.command()
@click.option('-v', '--verbose', count=True)
def checkconfig(verbose):
    if isinstance(CONFIG, dict):
        if verbose >= 2:
            print(ruamel.yaml.YAML().dump(CONFIG, sys.stdout))
        print('Config is good')


@main.command()
@click.option('-g', '--group')
def run(group: str = ""):
    pass


@main.command()
@click.argument('name', required=True)
def create_group(name: str = None):
    group_data: Dict[str, Any] = {}
    if name:
        group_data['group_name'] = name
        group_data.update(_query_group_data(name))
        print(group_data)


if __name__ == "__main__":
    main()
