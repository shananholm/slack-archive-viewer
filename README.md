# Slack Archive Viewer

A simple and easy-to-use viewer for your archived Slack messages, created with the help of GPT.

![slack-archive-viewer](https://user-images.githubusercontent.com/319462/236436077-abe9c630-3cad-4f29-b634-7135c1b19267.png)

## Purpose

This Slack archive viewer was developed in response to the change in Slack's free plan that limited available history by time rather than messages. The viewer allows you to access and navigate archived data more easily than searching through countless folders of JSON files.

## Requirements

You will need the following:

- Your Slack archive in the format shown below
- A local web server (e.g., `npx http-server`)
- Python installed (to run `create_index_files.py`)

### Archive Format

The archive should have the following structure:

```
|- index.html (from this repo)
|- create_index_files.py (from this repo)
|- users.json
|- channels.json
|- channel-1 (folder)
   |- 2023-01-01.json
   |- 2023-01-02.json
   |- index.json (added by create_index_files.py)
   |- files (folder)
      |- attachment-1.pdf
|- channel-2 (folder)
...
```

## Set Up

1. Clone or download this repository.
2. Place your archived Slack data in the appropriate format.
3. Run `python create_index_files.py` to generate the `index.json` files for each channel.
4. Start your local web server with `npx http-server`.
5. Open a browser and navigate to `http://localhost:8081/index.html` or the address provided by the `http-server`.

## Usage

With the Slack Archive Viewer set up, you can now easily view and navigate your archived Slack messages in a user-friendly format. No more sifting through countless folders and JSON files.

## Customization

If you want to use this viewer with another archive format, you can make progress quickly by providing the GPT model with a sample of the data you're trying to display and the folder structure it is displayed in. Update the code as needed to support your specific data format.
