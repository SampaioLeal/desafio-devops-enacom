terraform {
  backend "s3" {
    bucket = "sampaiol-enacom-terraform-states"
    key    = "devops-challenge/terraform.tfstate"
    region = "us-east-2"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.26.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
  default_tags {
    tags = {
      Terraform = "true"
      Project   = "devops-challenge"
      Company   = "enacom"
    }
  }
}
