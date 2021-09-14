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

# doc.make_and_generate_ps(imperial)
doc.make_and_generate_ps(oxford)