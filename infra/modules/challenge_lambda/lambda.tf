data "aws_ecr_image" "devops_challenge" {
  repository_name = module.ecr_repository.repository_name
  image_tag       = "latest"
}

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "8.1.2"

  function_name = "enacom-devops-challenge-${var.environment}"
  description   = "Lambda function for the Enacom DevOps Challenge - ${var.environment}"
  package_type  = "Image"
  architectures = ["x86_64"]
  image_uri     = data.aws_ecr_image.devops_challenge.image_uri

  create_package = false

  environment_variables = var.environment_variables

  memory_size = 128
  timeout     = 30

  tags = {
    Environment = var.environment
  }
}

output "lambda_function_name" {
  value = module.lambda_function.lambda_function_name
}

output "lambda_function_invoke_arn" {
  value = module.lambda_function.lambda_function_invoke_arn
}