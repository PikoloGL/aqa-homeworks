"""
Implement adapter patter from_txt_to_html

for example, we have a such structure in txt:

name,last_name,age,salary
John,Malkovich,28,1000

I want to see:

<name>John</name>
<last_name>Malkovich</last_name>
.............

It should work with any file with such a structure
"""


class TextToHtmlAdapter:
    def __init__(self, input_text):
        self.input_text = input_text

    def convert_to_html(self):
        lines = self.input_text.split('\n')
        if not lines:
            return ""

        html = "<table>\n"
        header = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            html += "  <tr>\n"
            for i in range(len(header)):
                html += f"    <{header[i]}>{values[i]}</{header[i]}>\n"
            html += "  </tr>\n"
        html += "</table>"
        return html


if __name__ == '__main__':
    # Sample text data
    test_text = """name,last_name,age,salary
    John,Malkovich,28,1000
    Alice,Smith,32,1200"""

    # Create the adapter and convert to HTML
    adapter = TextToHtmlAdapter(test_text)
    html_output = adapter.convert_to_html()
    print(html_output)
