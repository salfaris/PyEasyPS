from pylatex.base_classes import CommandBase
from pylatex import Document, Command, Package
from pylatex.utils import NoEscape
import os

class EasyPS(Document):
    def __init__(self):
        super().__init__()
        self._title = None
        self._student_name = None
        self._course_name = None
        self._university_to_output = None
        self._show_title = None

        # Document class settings
        self.documentclass = Command(
            'documentclass',
            options=['12pt'],
            arguments=['article'])

        # Required packages
        self.preamble.append(Package('lipsum'))
        self.preamble.append(Package('mathptmx'))
        self.preamble.append(Package('geometry'))

        # Layout settings
        self.preamble.append(Command('geometry',
            arguments='a4paper, margin=1in'))
        self.preamble.append(Command('linespread',
            arguments='1.'))
        self.change_length(r'\parskip', '0.5em')

    def make_title(self):
        if not self._show_title:
            return

        title_text = rf'{self._student_name} --- Personal Statement for {self._course_name}'
        title_display_text = (
            r"""
            \begin{center}
                \parskip
                \baselineskip
                \parindent=0pt
                \bf %s \par   
            \end{center}
            """ % title_text)
        self.append(NoEscape(title_display_text))

    @property
    def title(self):
        return self._title

    @property
    def student_name(self):
        return self._student_name

    @property
    def course_name(self):
        return self._course_name

    @property
    def university_to_output(self):
        return self._university_to_output

    @property
    def show_title(self):
        return self._show_title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @student_name.setter
    def student_name(self, new_name):
        self._student_name = new_name

    @course_name.setter
    def course_name(self, new_course_name):
        self._course_name = new_course_name

    @university_to_output.setter
    def university_to_output(self, new_university_name):
        self._university_to_output = new_university_name

    @show_title.setter
    def show_title(self, is_show):
        if not isinstance(is_show, bool):
            raise TypeError('Expect boolean for `show_title`.')
        self._show_title = is_show

    def make_ps(self, make_tex=False):
        self.make_title()
        self.append(NoEscape(r'\lipsum[1-6]'))
        self.generate_pdf('main', clean_tex=False)

if __name__ == '__main__':
    
    doc = EasyPS()
    doc.student_name = 'Sal Faris'
    doc.course_name = 'MSc Advanced Computer Science'
    doc.show_title = True

    doc.make_ps()

    tex = doc.dumps()  # The document as string in LaTeX syntax