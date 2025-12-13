module "production_lambda" {
  source = "./modules/challenge_lambda"

  environment = "production"

  s3_bucket = aws_s3_bucket.challenge_bucket_production.arn

  environment_variables = {
    S3_BUCKET = aws_s3_bucket.challenge_bucket_production.bucket
  }
}