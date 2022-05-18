variable "aws_region" {
  default = "us-east-1"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMRaovivo"
}


variable "key_pair_name" {
  default = "my_key_pairs"  
}

variable "airflow_subnet_id" {
  default = "subnet-00fa24bce9fa30322"
}

variable "vpc_id" {
  default = "vpc-0649fc8174e4429ac"
}