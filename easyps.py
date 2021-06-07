import os

# from pylatex.base_classes import CommandBase
from pylatex import Document, Command, Package
from pylatex.utils import NoEscape

class EasyPS(Document):
    def __init__(self):
        super().__init__()
        self._title = None
        self._student_name = None
        self._uni_ps = {}

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

    def _make_title(self, course_name, is_show_title):
        if self._student_name is None:
            raise NameError("Expect student name to be not None.")
        if not is_show_title:
            return

        title_text = (
            rf'{self._student_name} ---'
            + rf'Personal Statement for {course_name}')

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


    def add_ps(self, *uni_ps):
        for ps in uni_ps:
            tex_name = os.path.splitext(ps['tex_filename'])[0]
            self._uni_ps[tex_name] = ps

    def make_ps(self, for_tex_filename, make_tex=True):
        try:
            tex_name = os.path.splitext(for_tex_filename)[0]
            ps = self._uni_ps[tex_name]
        except PsNotAddedError:
            raise
        
        self._make_title(ps['course_name'], ps['show_title'])
        
        tex_filename = ps['tex_filename']
        path_to_tex = f'content/{tex_filename}'
        
        # NOTE :- Add os.path to crawl for filenames and
        #       terminate before appending to docs to prevent
        #       pdflatex error.
        self.append(NoEscape(r'\input{%s}' % path_to_tex))
        self.generate_pdf('main', clean_tex=(not make_tex))

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, new_name):
        self._student_name = new_name

class NameError(Exception):
    pass

class PsNotAddedError(KeyError):
    def __init__(self):
        self.message = "Ps was not added."
        super().__init__(self.message)