from pyeasyps.pyeasyps import EasyPS, UniPsObject

doc = EasyPS(content_dir='./content')
doc.student_name = 'Salman Faris'

oxford = UniPsObject(
    tex_filename='oxford.tex',
    course_name='MSc Advanced Computer Science', 
    show_title=False)

imperial = UniPsObject(
    tex_filename='imperial.tex',
    course_name='MSc Computing Science', 
    show_title=True)

ucl = UniPsObject(
    tex_filename='ucl.tex',
    course_name='MSc Computer Science', 
    show_title=True)

warwick = UniPsObject(
    tex_filename='warwick4500.tex',
    course_name='MSc Computer Science', 
    show_title=True)

kcl = UniPsObject(
    tex_filename='kings4000.tex',
    course_name='MSc Advanced Computing', 
    show_title=False)

doc.make_and_add_ps(imperial)