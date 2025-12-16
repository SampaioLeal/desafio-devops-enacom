resource "aws_s3_bucket" "challenge_bucket_production" {
  bucket = "sampaiol-enacom-devops-challenge-production"

  lifecycle {
    prevent_destroy = true
  }
}

# resource "aws_s3_bucket" "challenge_bucket_staging" {
#   bucket = "sampaiol-enacom-devops-challenge-staging"

#   lifecycle {
#     prevent_destroy = true
#   }
# }
