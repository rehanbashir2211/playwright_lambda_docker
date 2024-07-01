# HTML to PDF Conversion in AWS Lambda using Docker and Playwright

This repository contains a Docker-based solution for converting HTML to PDF using the Playwright library in an AWS Lambda environment. The resulting PDF files are then uploaded to an S3 bucket.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your local machine
- AWS CLI configured with appropriate permissions
- An AWS S3 bucket created to store the generated PDF files

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rehanbashir2211/playwright_lambda_docker.git
    cd your-repository
    ```

2. **Build the Docker image**:
    ```sh
    docker build -t html-to-pdf-lambda .
    ```

3. **Run the Docker container** to install the Playwright library and other dependencies:
    ```sh
    docker run --rm -v $(pwd):/var/task html-to-pdf-lambda
    ```

## Usage

To convert an HTML file to PDF and upload it to S3:

1. **Prepare your HTML file**:
    Ensure you have an HTML file that you want to convert.

2. **Invoke the Lambda function locally**:
    ```sh
    curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
    ```

3. **Check your S3 bucket**:
    The converted PDF should now be in your specified S3 bucket.

## Deployment

To deploy this solution to AWS Lambda:

1. **Package the Lambda function**:
    ```sh
    zip -r function.zip .
    ```

2. **Create a new Lambda function** in the AWS Management Console or using AWS CLI with the `function.zip` file.

3. **Set environment variables** for your Lambda function, such as:
    - `BUCKET_NAME`: Your S3 bucket name

4. **Update the Lambda function's IAM role** to include permissions for S3 operations.


Ref: https://datapearls.org/
