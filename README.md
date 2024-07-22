# pyrancid
RANCID style network backups in python.... with a twist

## Done
# config loader

## TODO
Pydantic models for:
    - the config
    - pyrancid device type
        - hostname
        - mgmt-ip
        - connection type -  morespecific type overrides the profile connection type
            - telnet - scrapli
            - ssh - scrapli
            - netconf - ncclient
    - pyrancid types - profiles
        - connection type
            - telnet - scrapli
            - ssh - scrapli
            - netconf - ncclient
        - prompt-regex
        - elevate: bool ( cisco enable type mode)
        - elevate command
        - credentials: password store with have named credentials inital
          password, elevate password if needed and username


Nornir integration
    - inventory plugin
    - extend the scrapli plugin -- generic type
Celery integration
    - celery tasks will be a nornir job
    - nornir inventory filter will be defined to target host(s)

