module "ecr_repository" {
  source  = "terraform-aws-modules/ecr/aws"
  version = "3.1.0"

  repository_name = "devops-challenge-lambda-${var.environment}"
  repository_force_delete = true

  repository_image_tag_mutability = "MUTABLE"

  create_lifecycle_policy = false

  repository_lambda_read_access_arns = [module.lambda_function.lambda_function_arn]
}