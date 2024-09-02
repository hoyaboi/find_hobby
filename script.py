def printHtml(description):
    print('''
    <!DOCTYPE html>
    <html dir="ltr">
      <head>
        <link rel="stylesheet" href="./css/default.css">
        <link rel="stylesheet" href="./css/recommendation.css">
        <link rel="stylesheet" href="./css/header.css">
        <title>findhobby</title>
      </head>
      <body>
        <header>
          <h1><a href="../">Find Hobby</a></h1>
          <div id="lnb">
            <nav>
              <ul>
                <li><a href="about.py">About</a></li>
                <li><a href="source.py">Source</a></li>
                <li><a href="producer.py">Producer</a></li>
              </ul>
            </nav>
          </div>
        </header>
        <section>
          %s
        </section>
        <footer>숭실대학교 기계공학부 AI및데이터분석의기초 어드벤쳐디자인프로젝트</footer>
      </body>
    </html>
    ''' % description)
