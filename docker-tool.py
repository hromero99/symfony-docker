#!/usr/bin/env python
import yaml
import argparse


def get_current_docker_compose():
    with open('docker-compose.yaml', 'r') as docker_file:
        return yaml.load(docker_file, Loader=yaml.Loader)


def add_database_to_docker_compose(docker_compose_yaml):
    print(docker_compose_yaml['services'])
    docker_compose_yaml['services']['database'] = {
        'container_name': 'database_symfony',
        'image': 'postgres:10',

    }
    print(docker_compose_yaml['services'].keys())
    with open('docker-compose-2.yaml', "w") as new_docker_file:
        yaml.dump(docker_compose_yaml, new_docker_file)


arg_parser = argparse.ArgumentParser(description="Tool for help during docker deploy")
arg_parser.add_argument('--symfonyFolder',  dest="symfony_folder", help="Folder with current Symfony Project")
arguments_variables = vars(arg_parser.parse_args())

if not arguments_variables['symfony_folder']:
    print("[!]Warning using default value for Symfony folder")
    arguments_variables['symfony_folder'] = "symfony-project"

add_database_to_docker_compose(get_current_docker_compose())
