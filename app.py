#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_yacy.cdk_yacy_stack import CdkYacyStack


app = cdk.App()
acct = app.node.get_context("acct")
region = app.node.get_context("region")
env = cdk.Environment(account=acct, region=region)
CdkYacyStack(app, "CdkYacyStack", env=env)

app.synth()
