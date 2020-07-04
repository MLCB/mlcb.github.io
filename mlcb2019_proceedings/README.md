I wrote some code to build the proceedings from what EasyChair will provide using their "Proceedings Manager". 

Unfortunately (afaik) EasyChair does not provide a sensible way to extract proceedings paper metadata. I got around this using an advanced hacking technique called "copy-and-paste". Go to the "Papers" tab in EasyChair's Proceedings Manager and copy the table into Excel (yes I know). Hopefully this also works for you. Delete columns other than the paper ID, authors and title. To avoid messing up special characters, save as "UTF-16 Unicode text" to a file called "paper_list_utf16.txt". 

Now you can run "html_maker.py" (this requires the yattag python package) which will a) recode the UTF-16 to UTF-8 and b) generate `index.thml`. 

Note that the `papers` folder comes from the proceedings archive you can download from EasyChair. 

Good luck! 