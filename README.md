# Move Look App 

Move Look App is a Python program used to move Looks between Looker instances.

## Status and Support

This program is **NOT** supported or warranteed by Looker in any way. Please do not contact Looker support
for issues with this program. Issues can be logged via https://github.com/christelilaka/Move-Look-via-Looker-API/issues

## Installation

This program uses the Looker SDK for Python.
1. Install the [Looker SDK for Python](https://pypi.org/project/looker-sdk/)
2. Download the repository to your computer and navigate to the folder

## Usage

Update the `.ini` files in the `ini_files` folder. This program assumes that you have the same model, views, and explores on both instances.


* `$ python app.py -id 2253` where **2253** is the `id` of the Look that must be moved. We can use the `-id` or `--look_id` flag to only move one Look.
* `$ python app.py -li 12 18 54 230 1595` show how to move many Looks. We can use the `-li` or `--list_IDs` flag to move more than one Look, we separate the Look IDs by space.
