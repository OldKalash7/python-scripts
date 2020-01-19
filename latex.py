# SCRIPT FOR GENERATING AND COMPILING LATEX SOURCE FILES


from pylatex import Document, Section, Subsection, Command
from pylatex.utils import NoEscape


if __name__ == '__main__':

    # Generate doc name
    doc = Document(input('Enter doc name: '))

    # Generate title
    doc.preamble.append(Command('title', input('Enter doc title: ')))
    doc.preamble.append(Command('author', input("Enter author: ")))
    doc.preamble.append(Command('date', NoEscape(r'\today')))  # Set the date to today
    doc.append(NoEscape(r'\maketitle'))
    doc.append(Command('newpage'))  # New page after title

    # Generate table of contents
    doc.append(Command('tableofcontents'))
    doc.append(Command('newpage'))  # New page after table of contents

    # Generate sections and subsections
    number_sections = int(input('Introduce the number of sections: '))
    subsections = 0
    for i in range(number_sections):
        with doc.create(Section(input('Enter section name: '))):
            doc.append('texto')
        subsections = int(input("How many subsections?: "))
        if subsections > 0:
            for j in range(subsections):
                with doc.create(Subsection(input('Name of the subsection: '))):
                    doc.append('texto')

    # Generate bibliography TODO

    # Generate and compile tex file and pdf
    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

