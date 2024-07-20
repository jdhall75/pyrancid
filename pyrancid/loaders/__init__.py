from typing import List
from ruamel.yaml import YAML


def config_loader(locations: List[str]):
    """ load and merge all configs specified.  """
    whole_config = {}
    yaml = YAML(typ="safe")
    for config in locations:
        tmp_config = {}
        with open(config, "rt") as fp:
            tmp_config = yaml.load(fp.read())
            whole_config.update(tmp_config)

    return whole_config
