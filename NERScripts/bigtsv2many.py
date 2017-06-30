import csv


def main():
    path ="/home/wlane/PycharmProjects/Clinical_Concept_Extractor/NERResources/Data/dx_docs_filtered.tsv"
    documents = read_big_tsv(path)
    count = 0
    batch = list()
    for doc in documents:
        if count % 100 == 0:
            write_file(batch)
            batch = list()
        else:
            batch.append(doc)

def read_big_tsv(path):
    with open(path, "rb") as csvfile:
        elements = csv.reader(csvfile)
    pass

def write_file(batch):
    pass

if "__main__" == __name__:
    main()