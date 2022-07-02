from pyeasyps.pyeasyps import EasyPS, University

ps = EasyPS(content_dir='./content')
ps.student_name = 'Salman Faris'

oxford = University(
    tex_filename='oxford.tex',
    course_name='MSc Advanced Computer Science', 
    show_title=False)

imperial = University(
    tex_filename='imperial.tex',
    course_name='MSc Computing Science', 
    show_title=True)

ps.generate_ps(oxford, imperial)