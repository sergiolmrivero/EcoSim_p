#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of the class Model

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""
import yaml
from space import SpaceCreator


class Model:

    def __init__(self, yaml_file):
        """ Carrega as definicoes do arquivo yaml"""
        self.simulation = None
        self.init_file = yaml_file
        with open(self.init_file, "r") as read_file:
            self.yaml_defs = yaml.load(read_file)
        self.name = self.yaml_defs['model_name']
        self.spaces = dict()
        self.create_spaces()

    def create_spaces(self):
        """Acessa a SpaceFactory (SpaceCreator) e cria os espaços"""
        self.spaces_def = self.yaml_defs['spaces']
        self.spaces_factory = SpaceCreator(self, self.spaces_def)
        self.spaces = self.spaces_factory.spaces
