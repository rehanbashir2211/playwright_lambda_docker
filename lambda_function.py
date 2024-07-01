import boto3
import asyncio
from playwright.async_api import async_playwright


import os

import sys

s3 = boto3.client('s3', aws_access_key_id='*******', aws_secret_access_key='*****')

def handler(event, context):

    # ///tmp/output.docx
    print('here')
    output_bucket_name = 'test-bucket'
    output_file_key = 'folder/sample.pdf'

    url = 'https://www.sheldonbrown.com/web_sample1.html'
    pdf_path = '/tmp/output.pdf'

    asyncio.run(playwright_pdf(url, pdf_path))

    s3.upload_file(pdf_path, output_bucket_name, output_file_key)

    return {'True':True}


async def playwright_pdf(url, pdf_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.pdf(path=pdf_path,landscape=True)
        await browser.close()

