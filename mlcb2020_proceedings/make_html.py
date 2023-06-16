import pandas as pd
import yattag
import os
import shutil
import numpy as np

os.chdir('/Users/daknowles/Dropbox/service/mlcb/mlcb.github.io/mlcb2020_proceedings')
# Read the TSV file using pandas
df = pd.read_csv('mlcb2020_papers.txt', delimiter='\t')

# generate HTML
doc, tag, text, line = yattag.Doc().ttl()
doc.asis("""<!DOCTYPE HTML>	
      <head>
		<title>MLCB 2020 Proceedings</title>
		<meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
	</head>""")
with tag('html'):
    with tag('body', id = 'hello'):
        with tag("div", klass="container"):
            line("h2", "MLCB 2020 Proceedings")
            doc.asis("<p>The 15th Machine Learning in Computational Biology (MLCB) meeting was held virtually. For more information and recordings of the talks please see <a href='https://sites.google.com/cs.washington.edu/mlcb2020/'>here</a> </p>""")
            with tag('ul'):
                for index, row in df.iterrows():
                    pdf_name = row['Name of File']
                    first_author = row['Authors'].split(",")[0].split(" ")[-1]
                    paper_id = pdf_name.split("\\")[0]
                    paper_href = "Public_abstracts/%s" % pdf_name.replace("\\","_")
                    final_pdf = "papers/%s_%s_etal_2020.pdf" % (paper_id, first_author)
                    shutil.copyfile(paper_href, final_pdf)
                    with tag('li'):
                        line("i", row['Authors'] + ". ")
                        line("b", row['Paper Title'] + ". ")
                        line("a", "[pdf]", href=final_pdf)
                        supp = row["Name of Supplemenatary Material"]
                        if type(supp)==str: 
                            print(supp)
                            supp_href = "Public_abstracts/%s" % supp.replace("\\","_")
                            final_supp = "papers/%s_%s_etal_2020_supp.pdf" % (paper_id, first_author)
                            shutil.copyfile(supp_href, final_supp)
                            line("a", "[supplement]", href=final_supp)

                    
with open("index.html","wt") as f: 
    f.writelines(yattag.indent(doc.getvalue()))