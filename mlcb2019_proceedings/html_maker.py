import yattag
import pandas as pd

# convert Excel's UTF16 output to UTF8 for HTML viewing
with open("paper_list_utf8.txt","wt", encoding="utf-8") as output:
    with open("paper_list_utf16.txt","rt", encoding="utf-16") as f:
        output.write(f.read())

# read with pandas
papers = pd.read_csv("paper_list_utf8.txt", sep = "\t", encoding = "utf-8", names = ("id", "authors", "name"))

# generate HTML
doc, tag, text, line = yattag.Doc().ttl()
doc.asis("""<!DOCTYPE HTML>	
      <head>
		<title>MLCB 2019 Proceedings</title>
		<meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
	</head>""")
with tag('html'):
    with tag('body', id = 'hello'):
        with tag("div", klass="container"):
            line("h2", "MLCB 2019 Proceedings")
            doc.asis("<p>The 14th Machine Learning in Computational Biology (MLCB) meeting, sponsored by Recursion, Deep Genomics, and Amazon, was held December 13-14th, 2019 co-located with NeurIPS in Vancouver. For more information, please see <a href='https://sites.google.com/cs.washington.edu/mlcb2019/'>here</a>. <a href='https://www.youtube.com/playlist?list=PL9Uzhlxi3pANDAzI_5NA-DJhmqUWhtqbz'>Recorded invited and contributed talks</a> are also available. </p>""")
            with tag('ul'):
                for row in papers.itertuples(): 
                    paper_href = "papers/paper_%i.pdf" % row.id
                    with tag('li'):
                        line("i", row.authors + ". ")
                        line("b", row.name + ". ")
                        line("a", "[pdf]", href=paper_href)
                    
with open("index.html","wt") as f: 
    f.writelines(yattag.indent(doc.getvalue()))