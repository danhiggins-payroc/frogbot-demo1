# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name-123456"  # Ensure the name is unique
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
