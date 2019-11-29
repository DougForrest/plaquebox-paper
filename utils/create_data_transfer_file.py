import requests

urls = ["https://zenodo.org/record/1470797/files/Dataset%201a%20Development_train.zip?download=1",
        "https://zenodo.org/record/1470797/files/Dataset%202%20Hold-out.zip?download=1",
        "https://zenodo.org/record/1470797/files/Dataset%203%20CERAD-like%20hold-out.zip?download=1"]


# outfile=
f = open(os.path.join("scripts", "downloadfiles.txt", "w")
f.write("TsvHttpData-1.0")
for url in urls:
    response = requests.head(url)
    print(url)
    print(response.headers)
    data = response.headers
    # print(response.headers['Content-Length'])
    f.write("\n")
    f.write("{}      {}      {}".format(url, data['Content-Length'], data['ETag']))