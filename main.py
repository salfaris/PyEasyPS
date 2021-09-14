from pyeasyps.pyeasyps import EasyPS, UniPsObject

ps = EasyPS(content_dir='./content')
ps.student_name = 'Salman Faris'

oxford = UniPsObject(
    tex_filename='oxford.tex',
    course_name='MSc Advanced Computer Science', 
    show_title=False)

imperial = UniPsObject(
    tex_filename='imperial.tex',
    course_name='MSc Computing Science', 
    show_title=True)

ps.generate_ps(oxford, imperial)