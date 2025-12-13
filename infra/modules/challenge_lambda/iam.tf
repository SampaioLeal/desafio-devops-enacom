resource "aws_iam_policy" "s3_bucket" {
  name        = "devops-challenge-s3-bucket-access-${var.environment}"
  description = "Permite que a Lambda faça download e upload de arquivos no bucket S3"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:HeadObject"
        ]
        Resource = ["${var.s3_bucket}/*"]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "s3_bucket" {
  role       = module.lambda_function.lambda_role_name
  policy_arn = aws_iam_policy.s3_bucket.arn
}
