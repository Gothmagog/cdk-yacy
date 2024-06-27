from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkYacyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpcid = self.node.get_context("vpcid")
        vpc = ec2.Vpc.from_lookup(self, "vpc", vpc_id=vpcid)
        
