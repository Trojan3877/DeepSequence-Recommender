provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "model_bucket" {
  bucket = "deepsequence-model-storage"
}