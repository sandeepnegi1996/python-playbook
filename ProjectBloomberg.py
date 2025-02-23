import csv
import requests

# with open('employee_birthday.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')
    



# writring to csv 

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# 1. make http call to a website 
response = requests.get('https://jsonplaceholder.typicode.com/posts')

postsResponse =[]
if response.status_code == 200:
    postsResponse = response.json()
    # print(postsResponse)
else:
    print(f'Failed to retrieve data: {response.status_code}')


with open('postsData.json',mode = 'w') as jsonfile:
     jsonfile.write('[')
     for post in postsResponse:
       jsonfile.write(f'{post}\n')
     jsonfile.write(']')
     


# 2. get the data from the website and store it in a file

# download files from a website 
# https://maven-datasets.s3.us-east-1.amazonaws.com/Spotify+Streaming+History/Spotify+Streaming+History.zip



import requests
import os

# URL of the file to download
url = 'https://maven-datasets.s3.us-east-1.amazonaws.com/Spotify+Streaming+History/Spotify+Streaming+History.zip'

# Directory to save the downloaded file
download_dir = 'downloads'

# Create the directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url,stream=True)
    print(f'response headers : {response.headers}')

        
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f'Successfully downloaded {url}')
    else:
        print(f'Failed to download {url}: {response.status_code}')

# Download the file
file_name = os.path.basename(url)
save_path = os.path.join(download_dir, file_name)
# download_file(url, save_path)





# as of now we are just downloading the whole file 
# we can download the file in chunks
# this is useful when we are downloading large files
# example: downloading a video file, we can download it in chunks and play it while downloading
# example 2: downloading a zip file, we can unzip it while downloading
# example 3: downloading a large file, we can download it in chunks and process it while downloading
# example 4: downloading a large file, we can download it in chunks and save it in a database while downloading

def download_file_in_chunks(url, save_path, chunk_size=1024):
    response = requests.get(url, stream=True)
    print(f'response headers : {response.headers}')
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
        print(f'Successfully downloaded {url}')
        print(f'Failed to download {url}: {response.status_code}')

# download_file_in_chunks(url, save_path)




#https://dummyjson.com/users




# response = requests.get('https://dummyjson.com/users')
# print(response.json())





# auth endpoint 
# 'https://dummyjson.com/auth/login'

import requests
import json
body= {'username': 'emilys',
       'password': 'emilyspass'}

json_data = json.dumps(body)
headers = {'Content-Type': 'application/json'}

response = requests.post("https://dummyjson.com/auth/login", 
    data=json_data,
    headers=headers )

print(response.json())