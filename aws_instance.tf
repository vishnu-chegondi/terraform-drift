data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}


resource "aws_instance" "terraform" {
    instance_type = "t3.micro"
    ami = data.aws_ami.ubuntu.id
    tags = {
        Name = "Test"
    }
}


resource "aws_instance" "test2" {
  instance_type = "t3.micro"
  ami = data.aws_ami.ubuntu.id
    tags = {
        Name = "Test2"
    }
}