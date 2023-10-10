#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """returns dictionary description of simple data structure"""
    return (obj.__dict__)
