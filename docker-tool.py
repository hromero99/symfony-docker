#!/usr/bin/env python
import yaml
import argparse
import json
import string
# Getting default docker-compose file
with open('docker-compose.yaml', 'r') as docker_file: docker_compose_content = yaml.load(docker_file, Loader=yaml.Loader)

# Getting services.json for some container implementations
with open('services.json', 'r') as services_file: services_file_content = json.load(services_file)


def add_database_to_docker_compose(database_backend):
    docker_compose_content['services']['database'] = services_file_content[database_backend]
    if arguments_variables['symfony_folder']:
        new_volumes_php = []
        for volume in docker_compose_content['services']['php']['volumes']:
            if volume.split(":")[0] == './symfony-project/':
                final_volume = "{}:{}".format(arguments_variables['symfony_folder'], volume.split(":")[1])
                new_volumes_php.append(final_volume)
            else:
                new_volumes_php.append(volume)
        docker_compose_content['services']['php']['volumes'] = new_volumes_php
        new_volumes_apache = []
        for volume in docker_compose_content['services']['apache']['volumes']:
            if volume.split(":")[0] == './symfony-project/':
                final_volume = "{}:{}".format(arguments_variables['symfony_folder'], volume.split(":")[1])
                new_volumes_apache.append(final_volume)
            else:
                new_volumes_apache.append(volume)
        docker_compose_content['services']['apache']['volumes'] = new_volumes_apache



    with open("docker-compose-2.yml", "w") as new_docker_compose:
        yaml.dump(data=docker_compose_content, stream=new_docker_compose, Dumper=yaml.Dumper)


arg_parser = argparse.ArgumentParser(description="Tool for help during docker deploy")
arg_parser.add_argument('--symfonyFolder',  dest="symfony_folder", help="Folder with current Symfony Project")
arg_parser.add_argument('--database', dest='database_backend', help="Backend for symfony database")
arg_parser.add_argument('--output', dest='output_file', help="docker-compose output name")

arguments_variables = vars(arg_parser.parse_args())

if not arguments_variables['symfony_folder']:
    print("[!]Warning using default value for Symfony folder")
    arguments_variables['symfony_folder'] = "symfony-project"


if arguments_variables['database_backend']:
    if arguments_variables['database_backend'] not in ['mysql', 'postgres']:
        raise Exception("[!]Available databases are mysql and Postgresql ")
    add_database_to_docker_compose(database_backend=arguments_variables['database_backend'])

if not arguments_variables['output_file']:
    print("[!]Warning using default value for output file")
    arguments_variables['output_file'] = "docker-compose-2.yml"

