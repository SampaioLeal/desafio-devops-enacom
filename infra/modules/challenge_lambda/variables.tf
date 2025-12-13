variable "environment" {
  type        = string
  description = "The environment for the Lambda Function"
}

variable "environment_variables" {
  type        = map(string)
  description = "Environment variables for the Lambda Function"
}

variable "s3_bucket" {
  type        = string
  description = "The S3 bucket used to download and upload artifacts"
}