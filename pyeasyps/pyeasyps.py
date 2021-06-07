import os

from pylatex import Document, Command, Package
from pylatex.utils import NoEscape

from .custom_warnings import StudentNameError

class EasyPS(Document):
    def __init__(self, student_name=None, content_dir='./content'):
        super().__init__(lmodern=False)
        self._student_name = student_name
        self._content_dir = content_dir

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
        
    def make_and_add_ps(self, uni_obj, make_tex=False):
        self._make_title(uni_obj.course_name, uni_obj.show_title)
        
        # Create `content_dir` if it does not exists.
        if not os.path.exists(self._content_dir):
            os.makedirs(self._content_dir)
        
        tex_filename = uni_obj.tex_filename
        path_to_tex = f'{self._content_dir}/{tex_filename}'

        if tex_filename not in os.listdir(self._content_dir):
            err_msg = (f"Cannot find TeX file '{tex_filename}' in " 
                       + f"content directory '{self._content_dir}'")
            raise FileNotFoundError(err_msg)
        
        self.append(NoEscape(r'\input{%s}' % path_to_tex))
        
        pdf_filename = 'ps_' + os.path.splitext(tex_filename)[0]
        self.generate_pdf(pdf_filename, clean_tex=(not make_tex))
        
    def _make_title(self, course_name, is_show_title):
        if self._student_name is None:
            raise StudentNameError("Expect student name to be not None.")
        if not is_show_title:
            return

        title_text = (
            f'{self._student_name} ---'
            + f' Personal Statement for {course_name}')

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
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, student_name):
        self._student_name = student_name
        
    @property
    def content_dir(self):
        return self._content_dir
    
    @content_dir.setter
    def content_dir(self, content_dir):
        self._content_dir = content_dir


class UniPsObject:
    def __init__(self, tex_filename=None, course_name=None, show_title=None):
        self._tex_filename = tex_filename
        self._course_name = course_name
        self._show_title = show_title
        
    @property
    def tex_filename(self):
        return self._tex_filename
    
    @property
    def course_name(self):
        return self._course_name
    
    @property
    def show_title(self):
        return self._show_title
