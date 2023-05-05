# slack-archive-viewer
Very simple GPT-generated Slack archive viewer

![slack-archive-viewer](https://user-images.githubusercontent.com/319462/236436077-abe9c630-3cad-4f29-b634-7135c1b19267.png)


## Why?
I was using Slack for a couple of very small community projects at the time that the free plan changed to limit available history by time, rather than messages. I downloaded an archive of messages and available files before they expired, stored them, and then forgot about them. When the need to access some of the archived data came up, I tried using ChatGPT as a coding friend and in the end used the GPT output alone with a number of iterations to refine and fix the one-page archive viewer.

# Requirements
This is designed for the archive format I had locally, which consisted of a file structure like this:
<pre>
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
</pre>

You'll also need a local webserver and Python (to run create_index_files.py) or patience to create the index files another way.

# Set up

The view relies on an `index.json` fpr each channel to be present in the folder structure. It wasn't in the archive, but it was easy enough to generate one as `create_index_files.py` and running this once will add these files. There are other ways to generate these, but the resulting format should be an array of JSON archives for each channel:
```
[
  "2023-04-04.json",
  "2023-04-05.json",
  "2023-06-26.json",
  "2023-06-27.json"
]
```

The only othe requirement is a local webserver, if running locally. It most likely won't run locally without a web server of some kind. I kept it simple with:
`npx http-server`
The open a browser to `http://localhost:8081/index.html` or whereever `http-server` tells you to go.

# What else?
There's nothing else, and there's not much to it. But it's definitely a lot easier to navigate than countless folders of JSON files.

If you want to repeat the experiment with another archived format, you can make a lot of progress quickly by supplying the GPT model with a sample of the data you're trying to display as well as the folder structure it is displayed in.
