#!/usr/bin/env python2

from setuptools import setup
import os
setup(
    name = 'openstack_opentracing',
    packages = ['openstack_opentracing', 'openstack_opentracing/test'],
    install_requires = [
        'jaeger_client==4.0.0',
        'opentracing_instrumentation==3.0.1',
        'opentracing==2.2.0',
        'oslo.middleware>=3.0.0',
        'oslo.config>=3.14.0',
        'oslo.service>=1.10.0',
        ],
    scripts = [],
    package_data = {},
    version='0.1.44'
)
