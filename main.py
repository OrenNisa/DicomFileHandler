import matplotlib.pyplot as plt
import pydicom
import dicom_csv
import csv


def main():
    # a. Extract the information from the file to the CSV file.
    dicom_data = dicom_csv.crawler.get_file_meta('dcm files/Home Ex.DCM')
    with open("dicom_csv.csv", "w") as f:
        writes = csv.writer(f)
        for value in dicom_data:
            for k, v in value.items():
                writes.writerow([k, v])

    # b. Show the image
    file = pydicom.read_file('dcm files/Home Ex.DCM')
    ct = file.pixel_array
    plt.figure()
    plt.imshow(ct.mean(axis=0), cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
